import sys
from lxml import html
from urllib.parse import urljoin
from slugify import slugify

URL_ROOT = 'http://catalog.shsu.edu/'
MAJOR_LIST_XPATH = '//*[@id="items"]/ul//li[contains(@class,"filter_23") and contains(@class,"filter_19")]'

root = html.parse(sys.stdin)
bachelors_list = root.xpath(MAJOR_LIST_XPATH)

for li in bachelors_list:
    program_name = li.xpath('./a/span/text()')[0]
    program_url = urljoin(URL_ROOT,li.xpath('./a/@href')[0])
    program_slug = slugify(program_name)
    sys.stdout.write(f'"{program_name}"|{program_url}|{program_slug}\n')
