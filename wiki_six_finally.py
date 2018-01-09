from urllib.request import urlopen
from bs4 import BeautifulSoup
import pymysql

conn = pymysql.connect(host='localhost', user='root', passwd='123456', db='mysql', charset='utf8')
cur = conn.cursor()

cur.execute('USE wikipedia')

class SolutionFound(RuntimeError):
    def __init__(self,message):
        self.message = message

# 获取指定页面的链接  并将链接转换为字典
def getLinks(fromPageId):
    cur.execute("SELECT toPageId FROM links WHERE fromPageId=%s", (fromPageId))
    if cur.rowcount == 0:
        return None
    else:
        return [x[0] for x in cur.fetchall()]  # x为字典


def constructDict(currentPage):
    links = getLinks(currentPage)
    if links:
        return dict(zip(links, [{}]*len(links)))
    return {}


