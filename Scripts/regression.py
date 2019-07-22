from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfTransformer, CountVectorizer, TfidfVectorizer
from Scripts.saveModels import saveModel, loadModel
from warnings import simplefilter
simplefilter(action='ignore', category=FutureWarning)

regr = Pipeline([('vect', CountVectorizer()), ('tfidf', TfidfTransformer()), ('clf', LogisticRegression(n_jobs=1, C=1e5)),])   

def REGRtrain(x_train, x_test, y_train, y_test):
    global regr
    regr.fit(x_train, y_train)
    saveModel(regr, 'logregression')

def REGRtrainResults(x_train, x_test, y_train, y_test, flairs):
    global regr
    regr.fit(x_train, y_train)
    y_pred = regr.predict(x_test)
    return accuracy_score(y_pred, y_test)
    # print('accuracy %s' % accuracy_score(y_pred, y_test))
    # print(classification_report(y_test, y_pred,target_names=flairs))

def REGRpredict(elem):
    regr = loadModel('logregression')
    x_test = [elem]
    y_pred = regr.predict(x_test)
    return y_pred[0]