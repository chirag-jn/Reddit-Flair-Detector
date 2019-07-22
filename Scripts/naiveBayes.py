from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfTransformer, CountVectorizer, TfidfVectorizer
from Scripts.saveModels import saveModel, loadModel

nb = Pipeline([('vect', CountVectorizer()), ('tfidf', TfidfTransformer()), ('clf', MultinomialNB()),])   

def NBtrain(x_train, x_test, y_train, y_test):
    global nb
    nb.fit(x_train, y_train)
    saveModel(nb, 'naiveBayes')

def NBtrainResults(x_train, x_test, y_train, y_test, flairs):
    global nb
    nb.fit(x_train, y_train)
    y_pred = nb.predict(x_test)
    return accuracy_score(y_pred, y_test)
    # print('accuracy %s' % accuracy_score(y_pred, y_test))
    # print(classification_report(y_test, y_pred,target_names=flairs))

def NBpredict(elem):
    nb = loadModel('naiveBayes') 
    x_test = [elem]
    y_pred = nb.predict(x_test)
    return y_pred[0]