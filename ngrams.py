from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import string
from collections import OrderedDict
from collections import Counter

# 分割数据生成列表，每一步截取列表的n个元素放到新的列表
def cleanContent(content):
    content = re.sub('\n+', ' ', content)  # 替换\n为空格
    content = re.sub(' +', ' ', content)  # 连续空格为一个空格
    content = re.sub('\[[0-9]*\]', ' ', content)
    content = bytes(content, 'UTF-8')  # 把内容转换成 UTF-8 格式以消除转义字符。
    content = content.decode('ascii', 'ignore')  # ascii编码
    cleanContentList = []
    content = content.split(" ")
    for item in content: # 去除单个字符不包括 i  a
        item = item.strip(string.punctuation)  # 去除标点符号(矫枉过正)
        if len(item) > 1 or (item.lower() == 'i' or item.lower() == 'a'):
            cleanContentList.append(item)
    return cleanContentList

def ngrams(content, n):
    content = cleanContent(content.upper())  # 统一按照大写处理
    output = []
    for i in range(len(content)-n+1):
        output.append(content[i:i+n])
    return output

html = urlopen("http://en.wikipedia.org/wiki/Python_(programming_language)")
bsObj = BeautifulSoup(html, "html.parser")

content = bsObj.find("div", {"id": "mw-content-text"}).get_text()
ngram_dic = {}
for ngrm in ngrams(content, 2):  # 统计列表元素频数
    num = ngrams(content, 2).count(ngrm)
    ngram_dic[str(ngrm)] = num  # 列表与字典不能作为字典的key，二者不可hash

# ngram_dic = Counter()
ngram_s = OrderedDict(sorted(ngram_dic.items(), key=lambda t: t[1], reverse=True)) # 按照value排序


print(ngram_s)
# print(str(len(ngram)))