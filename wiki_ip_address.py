from urllib.request import urlopen
from bs4 import BeautifulSoup
import datetime
import random
import re
import json

# 随机数据的种子
random.seed(datetime.datetime.now())

# 得到链接
def getLinks(articleUrl):
    html = urlopen("http://en.wikipedia.org" + articleUrl)
    bsObj = BeautifulSoup(html, "html.parser")
    # print(bsObj)
    return bsObj.find("div", {"id": "bodyContent"}).findAll("a", href=re.compile("^(/wiki/)((?!:).)*$"))

# 得到编辑历史ip
def getHistoryIps(pageUrl):
    pageUrl = pageUrl.replace("/wiki/", "")
    historyUrl = "http://en.wikipedia.org/w/index.php?title=" + pageUrl + "&action=history"
    print("history url is:" + historyUrl)
    html = urlopen(historyUrl)
    bsObj = BeautifulSoup(html, "html.parser")
    # 找出某一class的链接
    ipAddresses = bsObj.findAll("a", {"class": "mw-anonuserlink"})
    addressList = set()
    for ipaddress in ipAddresses:
        addressList.add(ipaddress.get_text())
    return addressList


def getIpCountry(ip):
    try:
        response = urlopen("http://freegeoip.net/json/"+ip).read().decode("utf-8")
    except HttpError:
        return None
    responseJson = json.loads(response)
    return responseJson.get("country_code")


links = getLinks("/wiki/Python_(programming_language)")
while len(links)>0:
    for link in links:
        print("---------------")
        historyIps = getHistoryIps(link.attrs["href"])
        for historyIp in historyIps:
            country = getIpCountry(historyIp)
            if country is not None:
                print(historyIp + " is from " + country)
    newLink = links[random.randint(0,len(links)-1)].attrs["href"]
    links = getLinks(newLink)