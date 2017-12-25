from bs4 import BeautifulSoup
from urllib.request import urlopen
import datetime
import random
import re

'''
一个函数 getLinks ，可以用维基百科词条 /wiki/< 词条名称 > 形式的 URL 链接作为参数，
然后以同样的形式返回一个列表，里面包含所有的词条 URL 链接。
• 一个主函数，以某个起始词条为参数调用 getLinks ，再从返回的 URL 列表里随机选择
一个词条链接，再调用 getLinks ，直到我们主动停止，或者在新的页面上没有词条链接
了，程序才停止运行。
'''

random.seed(datetime.datetime.now())
def getLinks(articleUrl):
    html = urlopen("http://en.wikipedia.org"+ articleUrl)
    bsObj = BeautifulSoup(html, "html.parser")
    return bsObj.find("div", {"id":"bodyContent"}).findAll("a", href=re.compile("^(/wiki/)((?!:).)*$"))

# links = getLinks("/wiki/Kevin_Bacon")
# while len(links)>0:
#     newArticle = links[random.randint(0, len(links)-1)].attrs["href"]
#     print(newArticle)
#     links = getLinks(newArticle)


pages = set()
def getPageLinks(pageUrl):
    global pages
    html = urlopen("http://en.wikipedia.org" + pageUrl)
    bsObj = BeautifulSoup(html, "html.parser")
    for link in bsObj.find("div", {"id":"bodyContent"}).findAll("a", href=re.compile("^(/wiki/)")):
        if "href" in link.attrs:
            if link.attrs["href"] not in pages:#鏈接去重
                #新的頁面
                newPage = link.attrs['href']
                print(newPage)
                pages.add(newPage)
                getPageLinks(newPage)  # 递归

# getPageLinks("")

'''创建一个爬虫来收
集页面标题、正文的第一个段落，以及编辑页面的链接（如果有的话）这些信息。'''
wikiPages = set()
def getWikiLinks(pageUrl):
    global wikiPages
    html = urlopen("http://en.wikipedia.org" + pageUrl)
    bsObj = BeautifulSoup(html, "html.parser")
    try:
        print("title: "+bsObj.h1.get_text())#题目
        print("firstP: "+bsObj.find(id="mw-content-text").findAll("p")[0].get_text())#第一段
        print("edit: "+bsObj.find(id="ca-edit").find("span").find("a").attrs['href'])#编辑链接
    except AttributeError:
        print("页面缺少一些属性！不过不用担心！")

    for link in bsObj.findAll("a", href=re.compile("^(/wiki/)")):
        if "href" in link.attrs:#a标签的href属性
            if link.attrs['href'] not in wikiPages:#链接去重
                new_page = link.attrs['href']
                print("-------------\n"+new_page)
                wikiPages.add(new_page)
                getWikiLinks(new_page)#递归 python一次行递归的次数要求小于1000次，不然崩溃

getWikiLinks("")
