import nltk

dataArr = []

def setData(dataList):
    global dataArr
    dataArr = []
    for i in dataList:
        dataArr.append((i, -1))


def vocabulary(dataList):
    global dataArr
    allWords = []
    for (words, sentiment) in dataArr:
        allWords.append(words)
    
    wordList = nltk.FreqDist(allWords)
    wordFeatures = wordList.keys()
    return wordFeatures

def extractFeatures(text):
    textWords = set(text)
    features = {}
    for word in wordFeatures:
        features['contains(%s)' % word] = (word in textWords)
    return features

wordFeatures = build