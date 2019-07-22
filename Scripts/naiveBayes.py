from sklearn.naive_bayes import MultinomialNB, GaussianNB
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfTransformer, CountVectorizer, TfidfVectorizer
import Scripts.analyzeText as dataset
import pandas as pd
import numpy as np

dataset.processText()
mapp = dataset.subreddits

flairs = ['Political', 'Non-Political', 'AskIndia', 'Reddiquette', 'Science & Technology', 'Policy & Economy', 'Finance & Business', 'Entertainment', 'Sports', 'Food', 'Photography', 'AMA']

topics_data = pd.DataFrame(mapp)

feature_combine = topics_data["title"] + topics_data["comments"] + topics_data["url"]

cat = topics_data['flair']
V = topics_data['comments']

x_train, x_test, y_train, y_test = train_test_split(V, cat, test_size=0.3, random_state=42)

nb = Pipeline([('vect', CountVectorizer()),
            ('tfidf', TfidfTransformer()),
            ('clf', MultinomialNB()),
            ])   

def train():
    global nb, x_train, y_train
    nb.fit(x_train, y_train)

# print(y_pred)
# print('accuracy %s' % accuracy_score(y_pred, y_test))
# print(classification_report(y_test, y_pred,target_names=flairs))

def predict(elem):
    global nb
    train()
    x_test = [elem]
    y_pred = nb.predict(x_test)
    return y_pred[0]