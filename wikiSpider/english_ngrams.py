from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import string
import operator


commonWords = ["the", "be", "and", "of", "a", "in", "to", "have", "it", "i", "that", "for", "you", "he", "with","on",
                   "do", "say", "this", "they", "is", "an", "at", "but", "we", "his", "from", "that", "not", "by",
                   "she",
                   "or", "as", "what", "go", "their", "can", "who", "get", "if", "would", "her", "all", "my", "make",
                   "about", "know", "will", "as", "up", "one", "time", "has", "been", "there", "year", "so", "think",
                   "when", "which", "them", "some", "me", "people", "take", "out", "into", "just", "see", "him", "your",
                   "come", "could", "now", "than", "like", "other", "how", "then", "its", "our", "two", "more", "these",
                   "want", "way", "look", "first", "also", "new", "because", "day", "more", "use", "no", "man", "find",
                   "here", "thing", "give", "many", "well"]

def cleanInput(input):
    input = re.sub('\n+', ' ', input)
    input = re.sub(' +', ' ', input)
    input = re.sub('\[[0-9]*\]', '', input)
    input = bytes(input, 'UTF-8')
    input = input.decode('ascii', 'ignore')
    input = input.split(' ')
    cleanoutput = []
    for item in input:
        item = item.strip(string.punctuation)
        if len(item)>1 or (item.lower() == 'i' or item.lower() == 'a'):
            if item.lower() not in commonWords:
                cleanoutput.append(item)
    return cleanoutput


def ngrams(input, n):
    input = cleanInput(input)
    output = {}
    for i in range(len(input)-n+1):
        ngramTemp = ' '.join(input[i:i+n])  # " ".join([]) 以空格为分隔符链接列表元素生成新的字符串
        if ngramTemp not in output:  # 字典值计数
            output[ngramTemp] = 0
        output[ngramTemp] += 1
    return output

def isCommen(ngram):
    global commonWords
    for word in ngram:
        if word in commonWords:
            return True
    return False

content = str(urlopen('http://pythonscraping.com/files/inaugurationSpeech.txt').read(), 'utf-8')
ngrams = ngrams(content, 2)
sorted_narams = sorted(ngrams.items(), key = operator.itemgetter(1), reverse=True)

print(sorted_narams)