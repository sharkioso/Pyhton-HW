import datetime
import logging
import gzip
import re


from Stats import calculate_statistics
from urllib.request import urlopen
from urllib.parse import urlparse
from io import TextIOWrapper
from functools import wraps

log = logging.getLogger(__name__)

LOG_RE = re.compile(r'''
(?P<IP>(\d{1,3}\.){3}\d{1,3}) # IP
\s+-\s+-\s+ # skip ' - - '
\[(?P<TIMESTAMP>[^]]*)]
\s+
"(?P<REQUEST>[^"]+)"
\s+
(?P<STATUS>\d+)
\s+
(?P<SIZE>\d+)
\s+
"(?P<PEFERER>[^"]+)"
\s+
"(?P<USER_AGENT>[^"]+)"
\s+
(?P<PROCESS_TIME>\d+)?
\s*
''', re.VERBOSE)


def is_valid_url(url):
    try:
        result = urlparse(url)
        return all([result.scheme, result.netloc])
    except ValueError:
        return False


def parse_lod_to_dict(line):
    match = LOG_RE.match(line)
    return match.groupdict()


def parse_ints(parsed_dict):
    for field in ('STATUS', "SIZE", "PROCESS_TIME"):
        if field in parsed_dict:
            if parsed_dict[field] is None and field == 'PROCESS_TIME':
                continue
            parsed_dict[field] = int(parsed_dict[field])
    return parsed_dict


def parse_t_to_dt(parsed_dict):
    parsed_dict['DATETIME'] = (
        datetime.datetime.strptime(parsed_dict['TIMESTAMP'],
                                   '%d/%b/%Y:%H:%M:%S %z'))
    # day to day time Р С—Р ВµРЎР‚Р ВµР Р†Р ВµР В»Р С‘ Р Р† Р С•Р В±РЎР‰Р ВµР С”РЎвЂљ РЎРѓ Р С”Р С•РЎвЂљР С•РЎР‚РЎвЂ№Р С Р СР С•Р В¶Р Р…Р С• РЎР‚Р В°Р В±Р С•РЎвЂљР В°РЎвЂљРЎРЉ
    return parsed_dict


REQUEST_RE = re.compile(r'''
    (?P<REQUEST_METHOD>[A-Z]+)\s(?P<REQUEST_URL>\S+)\sHTTP/
''', re.VERBOSE)


def parse_http_request(parsed_dict):
    parsed_dict.update(REQUEST_RE.match(parsed_dict['REQUEST']).groupdict())
    return parsed_dict


PARSERS = (parse_lod_to_dict, parse_ints, parse_t_to_dt, parse_http_request)


def parse_log_file(file, parsers=PARSERS):
    for line in file:
        try:
            parsed = line
            for parser in parsers:
                parsed = parser(parsed)
            yield parsed
        except Exception as e:
            log.warning(
                f'Exception during parsing file: {e}:{line}', exc_info=True)


def make_parser():
    import argparse
    parser = argparse.ArgumentParser('log_parser')
    parser.add_argument('--filename',
                        help='pass to file')
    parser.add_argument('--stat',
                        choices=['resource', 'client'],
                        default='resource')
    parser.add_argument('--lines', type=int)  # number of lines
    return parser


def auto_decompress(fn):
    @wraps(fn)
    def wrapper(path):
        if path.endswith('gz') and path:
            result = fn(path, mode='rb')
            return TextIOWrapper(gzip.GzipFile(fileobj=result),
                                 encoding='utf-8')
        return fn(path)

    return wrapper


@auto_decompress
def open_everything(path, mode='r'):
    if path.startswith('http'):
        if not is_valid_url(path):
            log.error(f"Invalid URL: {path}")
            raise ValueError(f"Invalid URL: {path}")
        try:
            return urlopen(path)
        except Exception as e:
            log.error(f"Failed to open URL {path}: {e}")
            raise
    else:
        try:
            return open(path, mode)
        except FileNotFoundError:
            log.error(f"File not found: {path}")
            raise


def main():
    parser = make_parser()
    args = parser.parse_args()

    with (open_everything(args.filename) as f):
        lines_to_read = args.lines

        if lines_to_read:
            limited_lines = (next(f) for _ in range(lines_to_read))
        else:
            limited_lines = f

        parsed_lines = parse_log_file(limited_lines)
        most_pop_resource, most_pop_client = calculate_statistics(parsed_lines)

        if args.stat == 'resource':
            log.warning(f"popular resource is {most_pop_resource}")
        else:
            log.warning(f"active client is {most_pop_client}")


if __name__ == "__main__":
    main()
