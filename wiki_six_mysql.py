'''
六度空间  mysql存储  从a页面链接到b页面
'''

from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import pymysql


# 链接数据库 并建立链接，游标指针  cur先执行execute选择返回结果然后进行下一步操作 先插入 再用lastrowid（最后一个插入的id）
conn = pymysql.connect(host="localhost", user="root", passwd="123456", db="mysql", charset="utf8")
cur = conn.cursor()
cur.execute("USE wikipedia")

# cur.execute("USE scraping")
# cur.execute("SELECT * FROM pages")
# cur.execute("INSERT INTO pages(title, content) VALUES (\"ghjk\", \"fghjk\")")
# print(cur.fetchone())
# print(cur.rowcount)
# print(cur.lastrowid)


# 判断url是否在数据库是否存储数据
def insertPageIfNotExits(url):
    cur.execute("SELECT * FROM pages WHERE url=%s", (url))  #从数据库中选择与url相同的记录
    if cur.rowcount == 0:
        cur.execute("INSERT INTO pages(url) VALUES (%s)", (url)) #插入到数据表中
        conn.commit()  #提交
        return cur.lastrowid  #返回最后插入的记录的id
    else:
        return cur.fetchone()[0] # 返回一条相同记录的id


#填写links表信息
def insertLinks(fromePageId, toPageId):
    cur.execute("SELECT * FROM links WHERE fromPageId=%s AND toPageId=%s", (int(fromePageId), int(toPageId)))  #选取该条件下的记录
    if cur.rowcount == 0: #如果不存在则插入
        cur.execute("INSERT INTO links(fromPageId, toPageId) VALUES (%s, %s)", (int(fromePageId), int(toPageId)))
        conn.commit()


'''
限制递归次数，获取链接。从某一页面开始，将页面插入到pages表，并返回fromPageId，解析该页面，获取该页面所有词条链接，
循环将词条链接插入pages，并返回toPageId,插入links，判断返回某一词条链接是否在在pages中没有则加入集合，并设置为新的采集页面，再放入到函数中执行，递归！
'''
pages = set()
def getLinks(pageUrl, recursionLevel):
    global pages
    if recursionLevel > 4:
        return
    pageId = insertPageIfNotExits(pageUrl)
    html = urlopen("http://en.wikipedia.org"+pageUrl)
    bsObj = BeautifulSoup(html, "html.parser")
    links = bsObj.findAll("a", href=re.compile("^(/wiki/)((?!:).)*$"))
    for link in links:
        pageIdB = insertPageIfNotExits(link.attrs['href'])  # link是解析出来的a标签，不要忘记取其href
        insertLinks(pageId, pageIdB)
        if link not in pages:
            newpage = link.attrs['href']
            pages.add(newpage)
            getLinks(newpage, recursionLevel+1)


getLinks("/wiki/Kevin_Bacon", 0)

cur.close()
conn.close()
