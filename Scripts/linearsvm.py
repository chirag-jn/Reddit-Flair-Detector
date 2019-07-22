from sklearn.linear_model import SGDClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfTransformer, CountVectorizer, TfidfVectorizer
from Scripts.saveModels import saveModel, loadModel

lsvm = Pipeline([('vect', CountVectorizer()), ('tfidf', TfidfTransformer()), ('clf', SGDClassifier(loss='hinge', penalty='l2',alpha=1e-3, random_state=42, max_iter=5, tol=None)),])   

def LSVMtrain(x_train, x_test, y_train, y_test):
    global lsvm
    lsvm.fit(x_train, y_train)
    saveModel(lsvm, 'linearsvm')

def LSVMtrainResults(x_train, x_test, y_train, y_test, flairs):
    global lsvm
    lsvm.fit(x_train, y_train)
    y_pred = lsvm.predict(x_test)
    return accuracy_score(y_pred, y_test)
    # print('accuracy %s' % accuracy_score(y_pred, y_test))
    # print(classification_report(y_test, y_pred,target_names=flairs))

def LSVMpredict(elem):
    lsvm = loadModel('linearsvm') 
    x_test = [elem]
    y_pred = lsvm.predict(x_test)
    return y_pred[0]