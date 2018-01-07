from urllib.request import urlopen
from random import randint


# 计算词单词的总数  也就是单词出现的次数
def wordListSum(wordlist):
    sum = 0
    for word, value in wordlist.items():
        sum += value
    return sum


# 随机返回单词字典中的一个单词
def retrieveRandomWord(wordlist):
    randIndex = randint(1, wordListSum(wordlist))
    for word, value in wordlist.items():  # 随机取值
        randIndex -= value
        if randIndex <= 0:
            return word


# 处理text 去除换行、引号 保证每个标点符号跟亲一个单词在一起，过滤空单词 新建词典以及单词的词典
def buildWordDict(text):
    text = text.replace('\n', ' ')
    text = text.replace('\"', ' ')

    punctuation = [',', '.', ';', ':']
    for symble in punctuation:
        text = text.replace(symble, " " + symble + " ")

    words = text.split(' ')
    words = [word for word in words if word != '']
    wordDict = {}
    for i in range(1, len(words)):
        if words[i-1] not in wordDict: # 判断当前单词是否在字典中
            wordDict[words[i-1]] = {}  # 为单词新建词典
        if words[i] not in wordDict[words[i-1]]: # 判断下一个单词是否在当前单词的词典中
            wordDict[words[i - 1]][words[i]] = 0  # 单词词典的下一个词赋值为0
        wordDict[words[i - 1]][words[i]] += 1  # 单词词典的下一个词增加1

    return wordDict

text = str(urlopen("http://pythonscraping.com/files/inaugurationSpeech.txt").read(), 'utf-8')
wordDict = buildWordDict(text)
length = 100
chain = ""
currentWord = 'I'
for i in range(0, length):
    chain += currentWord + " "
    currentWord = retrieveRandomWord(wordDict[currentWord])
print(chain)
# print(text)