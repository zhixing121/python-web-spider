from urllib.request import urlopen
from bs4 import BeautifulSoup
import random
from datetime import datetime
import pymysql
import re

basical_url = "http://en.wikipedia.org" #链接
basic_page_url = "/wiki/Kevin_Bacon"

#链接数据库
conn = pymysql.connect("localhost", "root", "123456", "mysql", charset='utf-8')
cur = conn.cursor()
cur.execute("USE scraping")

# 随机数种子
random.seed(datetime.now())

#存储数据
def store_data(title, content):
    cur.execute("INSERT INTO pages(title, content) VALUES(\"%s\", \"%s\"), (title, content)")
    cur.connection.commit()   #向数据库提交


#解析初始链接,并得到该初始页面中的其他词条链接
def getLinks(basical_url, basic_page_url):
    #解析链接
    html = urlopen(basical_url + basic_page_url)
    bsObj = BeautifulSoup(html, "html.parser")
    title = bsObj.find("h1").get_text()
    content = bsObj.findAll("div", {'id': 'mw-content-text'}).findAll('p').get_text()
    store_data(title, content)
    return bsObj.find("div", {"id": "bodyContent"}).findAll("a", href=re.compile('^(/wiki/)((?!:).)*$'))


links = getLinks(basical_url, basic_page_url)

while len(links)>0:
    for arcticleurl in getLinks(basical_url, basic_page_url):
    print(arcticleurl.attrs['href'])


