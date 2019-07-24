from Scripts.naiveBayes import NBpredict
from Scripts.linearsvm import LSVMpredict
from Scripts.regression import REGRpredict
from Scripts.randomforest import Forestpredict
from Scripts.mlpclassifier import MLPpredict

def predictflair(data):
    # Running Random Forest Algorithm for predicting data
    return Forestpredict(data['title'] + data['comments'])