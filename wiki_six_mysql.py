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