from Scripts.naiveBayes import NBtrain
from sklearn.model_selection import train_test_split
import Scripts.analyzeText as dataset
import pandas as pd

def train():
    dataset.processText()
    mapp = dataset.subreddits

    flairs = ['Political', 'Non-Political', 'AskIndia', 'Reddiquette', 'Science & Technology', 'Policy & Economy', 'Finance & Business', 'Entertainment', 'Sports', 'Food', 'Photography', 'AMA']

    topics_data = pd.DataFrame(mapp)

    feature_combine = topics_data["title"] + topics_data["comments"] + topics_data["url"]

    cat = topics_data['flair']
    V = topics_data['comments']
    x_train, x_test, y_train, y_test = train_test_split(V, cat, test_size=0.3, random_state=42)
    NBtrain(x_train, x_test, y_train, y_test)

train()