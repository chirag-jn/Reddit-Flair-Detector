import pymongo as pym
import dns
import Scripts.redditKeys as rkey
from pickle import dumps, loads
# from joblib import dump

url = 'mongodb+srv://' + rkey.mongoDB_Username + ':' + rkey.mongoDB_pass + '@redditflaircluster-jakts.mongodb.net/test?retryWrites=true&w=majority'

myClient = pym.MongoClient(url)
redditDB = myClient["redditflair"]
modelDB = redditDB["modelData"]

def saveModel(model, model_name):
    print('Saving Model:', model_name)
    global modelDB
    # dump(model, model_name+'.joblib')
    saved_model = dumps(model)
    modelDB.insert_one({model_name: saved_model, 'name': model_name})
    print('Model Saved:', model_name)

def loadModel(model_name):
    print('Loading Model:', model_name)
    global modelDB
    data = modelDB.find({'name': model_name})
    json_data = {}
    for i in data:
        json_data = i
    saved_model = json_data[model_name]
    print('Model Loaded:', model_name)
    return loads(saved_model)