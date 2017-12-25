
#一页wiki词条中的所有词条链接链接
from bs4 import BeautifulSoup
from urllib.request import urlopen
import re

html = urlopen("http://en.wikipedia.org/wiki/Kevin_Bacon")
wikiobj = BeautifulSoup(html, "html.parser")

for link in wikiobj.find("div", {"id": "bodyContent"}).findAll("a", href=re.compile("^(/wiki/)((?!:).)*$")):
    if "href" in link.attrs:
        print(link.attrs["href"])

