from urllib.request import urlretrieve
from urllib.request import urlopen
from bs4 import BeautifulSoup
import os

downloadDirectory = "downloaded"
baseUrl = "http://pythonscraping.com"


def getAbsoluteUrl(baseUrl, source):  #获取
    if source.startswith("http://www."):
        url = "http://"+source[11:]
    elif source.startswith("http://"):
        url = source
    elif source.startswith("www."):
        url = "http://"+source[4:]
    else:
        url = baseUrl + "/" +source

    if baseUrl not in url:
        return None
    return url


def getDownloadPath(baseUrl, absoluteUrl, downloadDirectory):
    path = absoluteUrl.replace("www.", "")
    path = path.replace(baseUrl, "")
    path = downloadDirectory + path
    directory = os.path.dirname(path)

    if not os.path.exists(directory):
         os.makedirs(directory)
    return path


html = urlopen("http://www.pythonscraping.com")
bsObj = BeautifulSoup(html, "html.parser")

downloadList = bsObj.findAll(src=True)  #找到所有的src

for download in downloadList:
    fileUrl = getAbsoluteUrl(baseUrl, download["src"])  #从src获取绝对路径链接
    if fileUrl is not None:
        print(fileUrl)
