from urllib.request import urlopen
from bs4 import BeautifulSoup


url = "http://www.open-open.com/solution/view/1319458447249"
html = urlopen(url)
bsObj = BeautifulSoup(html, "html.parser")
scritptDiv = bsObj.findAll("div", {"class": "question-body"})[0].findAll("pre")#.find("div", {"class": "question-body"})
# print(bsObj)
spanList = []
for pre in scritptDiv:
    presc = pre.findAll("span")
    scriptstr = ""
    for span in presc:
        script = span.get_text()
        scriptstr += script
    spanList.append(scriptstr)
for scriptjs in spanList:
    print(scriptjs)
print(spanList[1])