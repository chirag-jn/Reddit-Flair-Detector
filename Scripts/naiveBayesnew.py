from sklearn.naive_bayes import MultinomialNB, GaussianNB
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfTransformer, CountVectorizer, TfidfVectorizer
import analyzeText as dataset
import pandas as pd
import numpy as np

dataset.processText()
mapp = dataset.subreddits

flairs = ['Political', 'Non-Political', 'AskIndia', 'Reddiquette', 'Science & Technology', 'Policy & Economy', 'Finance & Business', 'Entertainment', 'Sports', 'Food', 'Photography', 'AMA']

# print(len(mapp['flair']))
# x_train = mapp['flair'][:700]
# y_train = mapp['flair'][701:]
# x_test = mapp['author'][:700]
# y_test = mapp['author'][701:]

# nb = MultinomialNB()
# nb.fit(x_train, y_train)
# y_pred = nb.predict(x_test)
# print('accuracy %s' % accuracy_score(y_pred, y_test))
# print(classification_report(y_test, y_pred,target_names=flairs))


topics_data = pd.DataFrame(mapp)

# print(len(topics_data["title"]))
# print(len(topics_data["comments"]))
# print(len(topics_data["url"]))

# feature_combine = topics_data["title"] + topics_data["comments"]
# topics_data.replace(r'\s+', np.nan, regex=True)
# feature_combine = topics_data["title"] + topics_data["comments"] + topics_data["url"]
# topics_data = topics_data.assign(feature_combine = feature_combine)

cat = topics_data.flair
# V = topics_data.feature_combine
V = topics_data.title

x_train, x_test, y_train, y_test = train_test_split(V, cat, test_size=0.3, random_state=42)
# nb = MultinomialNB() 
nb = Pipeline([('vect', CountVectorizer()),
               ('tfidf', TfidfTransformer()),
               ('clf', MultinomialNB()),
              ])   
# print(len(x_train))
# print(len(y_train))
nb.fit(x_train, y_train)
# x_train_arr = np.array(x_train).reshape(-1,1)
# nb.fit(x_train_arr, y_train)
y_pred = nb.predict(x_test)
print('accuracy %s' % accuracy_score(y_pred, y_test))
print(classification_report(y_test, y_pred,target_names=flairs))