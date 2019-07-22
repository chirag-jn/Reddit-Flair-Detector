import pymongo as pym
import dns
import Scripts.redditKeys as rkey
from pickle import dumps, loads
from joblib import dump, load

url = 'mongodb+srv://' + rkey.mongoDB_Username + ':' + rkey.mongoDB_pass + '@redditflaircluster-jakts.mongodb.net/test?retryWrites=true&w=majority'

myClient = pym.MongoClient(url)
redditDB = myClient["redditflair"]
modelDB = redditDB["modelData"]

my_model = None

def saveModel(model, model_name):
    print('Saving Model:', model_name)
    global modelDB, my_model
    my_model = model
    # dump(model, model_name+'.joblib')
    # saved_model = dumps(model)
    # modelDB.insert_one({model_name: saved_model, 'name': model_name})
    print('Model Saved:', model_name)

def loadModel(model_name):
    print('Loading Model:', model_name)
    global modelDB
    # data = modelDB.find({'name': model_name})
    # json_data = {}
    # for i in data:
    #     json_data = i
    # saved_model = json_data[model_name]
    # global my_model
    print('Model Loaded:', model_name)
    # return loads(saved_model)
    return my_model