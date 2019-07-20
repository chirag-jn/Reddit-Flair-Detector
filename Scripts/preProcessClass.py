import re
from nltk.tokenize import word_tokenize
from string import punctuation
from nltk.corpus import stopwords

class preProcessText:
    def __init__(self):
        self._stopwords = set(stopwords.words('english') + list(punctuation) + ['AT_USER','URL'])
    
    def processTextList(self, listToProcess):
        finalList = []
        for item in listToProcess:
            finalList.append(self._processText(item))
        return finalList
    
    def _processText(self, text):
        text = text.lower()
        text = re.sub('((www\.[^\s]+)|(https?://[^\s]+))', 'URL', text) # remove URLs
        text = re.sub('@[^\s]+', 'AT_USER', text) # remove usernames
        text = re.sub(r'#([^\s]+)', r'\1', text) # remove the # in #hashtag
        text = word_tokenize(text) # remove repeated characters (helloooooooo into hello)
        return [word for word in text if word not in self._stopwords]