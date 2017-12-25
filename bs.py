from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

html = urlopen("http://www.pythonscraping.com/pages/page3.html")
bsobj = BeautifulSoup(html, "html.parser")
namelist = bsobj.find("img", {"src": "../img/gifts/img1.jpg"}).parent.previous_sibling.get_text()
# print(namelist)


# for name in namelist:
#     print(name)

# h = bsobj.find({"h1","h2","h3","h4","h5","h6"})
# print(h)

# re = [A-Za-z0-9\._+]+@[A-Za-z0-9]+\.(com|edu|org|net)

# imgs = bsobj.find_all("img", {"src":re.compile("\.\.\/img\/gifts\/img.*\.jpg")})
# for img in imgs:
#     print(img)

# imgs = bsobj.find_all("img")
# for img in imgs:
#     print(img.attrs["src"])

tags = bsobj.findAll(lambda tag: len(tag.attrs) == 2)
for tag in tags:
    print(tag,"-"*50)