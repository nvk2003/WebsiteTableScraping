import urllib.request
from pprint import pprint
from html_table_parser.parser import HTMLTableParser
import pandas as pd

# Opens a website and read its contents
def url_get_contents(url):
    # making request to the website
    req = urllib.request.Request(url=url)
    f = urllib.request.urlopen(req)

    # reading contents of the website
    return f.read()

xhtml = url_get_contents('https://www.infoplease.com/geography/largest-countries-world').decode('utf-8')
# print(xhtml)

p = HTMLTableParser()
p.feed(xhtml)
pprint(p.tables[0])

print("\n\nFiltered Dataframe\n")
print(pd.DataFrame(p.tables[0]))






