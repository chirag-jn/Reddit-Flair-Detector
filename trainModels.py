from Scripts.naiveBayes import NBtrain, NBtrainResults
from sklearn.model_selection import train_test_split
import Scripts.analyzeText as dataset
import pandas as pd

def train():
    dataset.processText()
    mapp = dataset.subreddits
    topics_data = pd.DataFrame(mapp)
    feature_combine = topics_data["title"] + topics_data["comments"]
    outputs = topics_data['flair']
    inputs = feature_combine
    x_train, x_test, y_train, y_test = train_test_split(inputs, outputs, test_size=0.2, random_state=42)

    NBtrain(x_train, x_test, y_train, y_test)

def getResults():
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
        acc_score = NBtrainResults(x_train, x_test, y_train, y_test, flairs)
        print(input_labels[i], ':', acc_score)

train()