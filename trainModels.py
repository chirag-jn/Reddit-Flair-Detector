from Scripts.naiveBayes import NBtrain, NBtrainResults
from Scripts.linearsvm import LSVMtrain, LSVMtrainResults
from Scripts.regression import REGRtrain, REGRtrainResults
from Scripts.randomforest import Foresttrain, ForesttrainResults
from Scripts.mlpclassifier import MLPtrain, MLPtrainResults
from sklearn.model_selection import train_test_split
import Scripts.analyzeText as dataset
import pandas as pd

def train():
	# Function used to train the desired model. We are using Random Forest as our model.
    dataset.processText()
    mapp = dataset.subreddits
    topics_data = pd.DataFrame(mapp)
    feature_combine = topics_data["title"] + topics_data["comments"]
    outputs = topics_data['flair']
    inputs = feature_combine
    x_train, x_test, y_train, y_test = train_test_split(inputs, outputs, test_size=0.2, random_state=42)

    Foresttrain(x_train, x_test, y_train, y_test)

def getResults():
	# Function to check the accuracy which we get after running various algorithms on various parameters.
    dataset.processText()
    mapp = dataset.subreddits
    flairs = ['Political', 'Non-Political', 'AskIndia', 'Reddiquette', 'Science & Technology', 'Policy & Economy', 'Finance & Business', 'Entertainment', 'Sports', 'Food', 'Photography', 'AMA']
    topics_data = pd.DataFrame(mapp)
    outputs = topics_data['flair']

    input_features = [topics_data['comments'], topics_data['author'], topics_data['title'], topics_data['body'], topics_data['id'], topics_data['url'], topics_data['comms_num'], topics_data['score'], topics_data['title'] + topics_data['comments'] + topics_data['url'], topics_data['title'] + topics_data['comments']]
    input_labels = ['Comments', 'Author', 'Title', 'Body', 'ID', 'URL', 'Number of Comments', 'Score', 'Title + Comments + URL', 'Title + Comments']
    
    for i in range(len(input_features)):
        inputs = input_features[i]
        x_train, x_test, y_train, y_test = train_test_split(inputs, outputs, test_size=0.2, random_state=42)
        acc_score = ForesttrainResults(x_train, x_test, y_train, y_test, flairs)
        print(input_labels[i], ':', acc_score)

if __name__=='__main__':
        train()