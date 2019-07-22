from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfTransformer, CountVectorizer, TfidfVectorizer
from Scripts.saveModels import saveModel, loadModel

forest = Pipeline([('vect', CountVectorizer()), ('tfidf', TfidfTransformer()), ('clf', RandomForestClassifier(n_estimators = 1000, random_state = 42)),])   

def Foresttrain(x_train, x_test, y_train, y_test):
    global forest
    forest.fit(x_train, y_train)
    saveModel(forest, 'randomforest')

def ForesttrainResults(x_train, x_test, y_train, y_test, flairs):
    global forest
    forest.fit(x_train, y_train)
    y_pred = forest.predict(x_test)
    return accuracy_score(y_pred, y_test)
    # print('accuracy %s' % accuracy_score(y_pred, y_test))
    # print(classification_report(y_test, y_pred,target_names=flairs))

def Forestpredict(elem):
    forest = loadModel('randomforest') 
    x_test = [elem]
    y_pred = forest.predict(x_test)
    return y_pred[0]