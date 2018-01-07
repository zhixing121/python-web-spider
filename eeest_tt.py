dict = {'ddd': {'rrr': 0, 'ttt': 0, 'ggg': 3}, 'yyy': {'tt': 0, 'rr': 1}, 'yt':{}}

# print(dict)

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
        wordDict[words[i - 1]][words[i]] = wordDict[words[i - 1]][words[i]] + 1  # 单词词典的下一个词增加1

    return wordDict

# text = str(urlopen("http://pythonscraping.com/files/inaugurationSpeech.txt").read(), 'utf-8')
text = '''Called from a retirement which I had supposed was to continue for the residue of my life to fill the chief executive office of this great and free nation, I appear before you, fellow-citizens, to take the oaths which the Constitution prescribes as a necessary qualification for the performance of its duties; and in obedience to a custom coeval with our Government and what I believe to be your expectations I proceed to present to you a summary of the principles which will govern me in the discharge of the duties which I shall be called upon to perform.

It was the remark of a Roman consul in an early period of that celebrated Republic that a most striking contrast was observable in the conduct of candidates for offices of power and trust before and after obtaining them, they seldom carrying out in the latter case the pledges and promises made in the former. However much the world may have improved in many respects in the lapse of upward of two thousand years since the remark was made by the virtuous and indignant Roman, I fear that a strict examination of the annals of some of the modern elective governments would develop similar instances of violated confidence.'''
wordlist = buildWordDict(text)
print(wordlist)