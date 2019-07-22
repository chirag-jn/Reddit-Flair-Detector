from Scripts.naiveBayes import NBpredict

def predictflair(data):
    return NBpredict(data['comments'])