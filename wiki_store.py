from urllib.request import urlopen
from bs4 import BeautifulSoup
import random
from datetime import datetime
import pymysql
import re

basical_url = "http://en.wikipedia.org" #链接
basic_page_url = "/wiki/Kevin_Bacon"

#链接数据库
conn = pymysql.connect(host="localhost", user="root", passwd="123456", db="mysql", port=3306, charset='utf8')
cur = conn.cursor()
# conn.set_charset('utf-8')
cur.execute("USE scraping")

# 随机数种子
random.seed(datetime.now())


# 存储数据
def store_data(title, content):
    cur.execute("INSERT INTO pages(title, content) VALUES(\"%s\", \"%s\")", (title, content))
    cur.connection.commit()   # 向数据库提交


# 解析初始链接,并得到该初始页面中的其他词条链接
def getLinks(basical_url, basic_page_url):
    #解析链接
    html = urlopen(basical_url + basic_page_url)
    bsObj = BeautifulSoup(html, "html.parser")
    title = bsObj.find("h1").get_text()
    content = bsObj.find("div", {'id': 'mw-content-text'}).find('p').get_text()
    store_data(title, content)
    return bsObj.find("div", {"id": "bodyContent"}).findAll("a", href=re.compile('^(/wiki/)((?!:).)*$'))


links = getLinks(basical_url, basic_page_url)
try:
    while len(links) > 0:
        articleurl = links[random.randint(0, len(links)-1)].attrs['href']  #选取随机链接
        print(articleurl)
        try:
            links = getLinks(basical_url, articleurl)
        except AttributeError:
            articleurl = links[random.randint(0, len(links) - 1)].attrs['href']
finally:
    cur.close()
    conn.close()

