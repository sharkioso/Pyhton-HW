import ssl
import sys
from urllib.parse import quote
from urllib.request import urlopen
import re

context = ssl.create_default_context()
# name = sys.argv[1]
print(sys.argv)

res = "Философия"

url = 'https://ru.wikipedia.org/wiki' + quote(res)
response = urlopen(url)
html_content = response.read().decode('utf-8', errors='ignore')

urls = re.split(r"\s+href=.*?>",html_content)
print(urls)
print(len(urls),type(urls))
'''student_names = {}

year_blocks = re.split(r"<h3>(.*?)</h3>", html_content, flags=re.DOTALL)

for i in range(1, len(year_blocks), 2):
    year = year_blocks[i].strip()
    content = year_blocks[i + 1]

    names = re.findall(r'<a\s+href=.*?>(.*?)</a>', content, flags=re.DOTALL)
    names = [name.strip() for name in names]

    student_names[year] = names
print(html_content)
print("1")
for year, names in student_names.items():
    print(year)
    for student in names:
        print(student)
    print(len(names))
    print()
'''