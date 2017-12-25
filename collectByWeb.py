from bs4 import BeautifulSoup
from urllib.request import urlopen
import re
import random
import datetime

pages = set()
random.seed(datetime.datetime.now())  #随机种子


# 获取页面所有内连的列表
def get_internal_links(bsObj, includeUrl):
    internalLinks = []
    # 找出所有以/为开头的链接
    for link in bsObj.findAll("a", href=re.compile("^(/|.*"+includeUrl+")")):
        if link .attrs["href"] is not None:
            if link.attrs["href"] not in internalLinks:
                internalLinks.append(link.attrs["href"])
    return internalLinks


# 获取页面所有外链的列表
def get_external_links(bsObj, externalUrl):
    externalLinks = []
    # 找出所有以http或者www开头且不包含当前Url的链接
    for link in bsObj.findAll("a",href=re.compile("^(http|www)((?!"+externalUrl+").)*$")):
        if link .attrs["href"] is not None:
            if link.attrs["href"] not in externalLinks:
                externalLinks.append(link.attrs["href"])
    return externalLinks


def split_address(address):
    address_parts = address.replace("http://", "").split("/")
    return address_parts


def get_random_external_link(starting_page):
    html = urlopen(starting_page)
    bsObj = BeautifulSoup(html, "html.parser")
    external_links = get_external_links(bsObj, split_address(starting_page)[0])
    if len(external_links)==0:
        internal_links = get_internal_links(bsObj, starting_page)
        return get_random_external_link(internal_links[random.randint(0, len(internal_links)-1)])
    else:
        return external_links[random.randint(0, len(external_links)-1)]


def follow_external_only(starting_site):
    external_link = get_random_external_link(starting_site)
    print("随机外链是:"+external_link)
    follow_external_only(external_link)


follow_external_only("http://oreilly.com")