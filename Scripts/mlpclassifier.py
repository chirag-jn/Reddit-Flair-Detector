from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfTransformer, CountVectorizer, TfidfVectorizer
from Scripts.saveModels import saveModel, loadModel
from warnings import simplefilter
from sklearn.exceptions import ConvergenceWarning
simplefilter(action='ignore', category=ConvergenceWarning)

mlp = Pipeline([('vect', CountVectorizer()), ('tfidf', TfidfTransformer()), ('clf', MLPClassifier(hidden_layer_sizes=(30,30,30))),])   

def MLPtrain(x_train, x_test, y_train, y_test):
    global mlp
    mlp.fit(x_train, y_train)
    saveModel(mlp, 'mlpclassifier')

def MLPtrainResults(x_train, x_test, y_train, y_test, flairs):
    global mlp
    mlp.fit(x_train, y_train)
    y_pred = mlp.predict(x_test)
    return accuracy_score(y_pred, y_test)
    # print('accuracy %s' % accuracy_score(y_pred, y_test))
    # print(classification_report(y_test, y_pred,target_names=flairs))

def MLPpredict(elem):
    mlp = loadModel('mlpclassifier') 
    x_test = [elem]
    y_pred = mlp.predict(x_test)
    return y_pred[0]