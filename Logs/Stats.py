from collections import Counter


def calculate_statistics(parsed_lines):
    resource_counter = Counter()
    client_counter = Counter()

    for line in parsed_lines:
        resource_counter[line['REQUEST_URL']] += 1
        client_counter[line['IP']] += 1

    most_popular_resource, _ = resource_counter.most_common(1)[0]
    most_popular_client, _ = client_counter.most_common(1)[0]

    return most_popular_resource, most_popular_client