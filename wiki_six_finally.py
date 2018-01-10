from urllib.request import urlopen
from bs4 import BeautifulSoup
import pymysql

conn = pymysql.connect(host='localhost', user='root', passwd='123456', db='mysql', charset='utf8')
cur = conn.cursor()

cur.execute('USE wikipedia')

class SolutionFound(RuntimeError):
    def __init__(self, message):
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

# print(constructDict(1))


'''
如果递归限制已经到达，就停止搜索，返回结果
如果函数获取的字典为空，则在当前页面进行搜索，如果当前链接也没有链接，则返回空字符串
如果当前页面包含我们搜索的页面链接，就把页面ID复制到递归的栈顶，然后抛出一个异常，显示页面已经找到。递归过程中每个栈都会打印当前页面ID，然后抛出异常显示页面已经找到，最终打印在页面上就是一个完整的页面ID路径表。
如果链接没找到，把递归限制减一，然后搜索函数调用下一层链接。
'''

# 链接树要么为空 要么包含多个链接
def searchDepth(targetPageId, currentPageId, linkTree, depth):
    if depth == 0:
        return linkTree
    if not linkTree:
        linkTree = constructDict(currentPageId)
        if not linkTree:
            return {}
    if targetPageId in linkTree.keys():
        print("TARGET:" + targetPageId + "FOUND!")
        raise SolutionFound("PAGE:" + str(currentPageId))

    for branchKey, branchValue in linkTree.items():
        try:
            linkTree[branchKey] = searchDepth(targetPageId, branchKey, branchValue, depth-1)
        except SolutionFound as e:
            print(e.message)
            raise SolutionFound("PAGE:" + currentPageId + "FOUND!")
    return linkTree


try:
    searchDepth('1222', '1214', {}, 4)
    print("No solution found!")
except SolutionFound as e:
    print(e.message)