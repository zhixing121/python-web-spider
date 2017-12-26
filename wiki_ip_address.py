from urllib.request import urlopen
from bs4 import BeautifulSoup
import datetime
import random
import re

# 随机数据的种子
random.seed(datetime.datetime.now())

# 得到链接
def getLinks(articleUrl):
    html = urlopen("http://en.wikipedia.org" + articleUrl)
    bsObj = BeautifulSoup(html, "html.parser")
    return bsObj.find("div", {"id", "bodyContent"}).findAll("a", href=re.compile('^(/wiki/)((?!:).)*$'))

# 得到编辑历史ip
def getHistoryIps():
