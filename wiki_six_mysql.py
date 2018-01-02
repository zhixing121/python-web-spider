'''
六度空间  mysql存储  从a页面链接到b页面
'''

from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import pymysql


# 链接数据库 并建立链接，游标指针


