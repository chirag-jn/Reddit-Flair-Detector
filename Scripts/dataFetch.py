import praw
import pandas as pd
import datetime as dt
import redditKeys as rkey

subredditName = 'india'
numberReddits = 100

flairs = ['Political', 'Non-Political', 'AskIndia', 'Reddiquette', 'Science & Technology', 'Policy & Economy', 'Finance & Business', 'Entertainment', 'Sports', 'Food', 'Photography', 'AMA']

def get_date(created):
    return dt.datetime.fromtimestamp(created)

def fetch_data():
    # Starting the Reddit API
    reddit = praw.Reddit(client_id = rkey.script,
                        client_secret = rkey.secret,
                        user_agent = rkey.name,
                        username = rkey.username,
                        password = rkey.password)

    subreddit = reddit.subreddit(subredditName)

    # Dictionary for storing the content fetched using the API
    topics_dict = { "flair":[], 
                    "title":[], 
                    "score":[], 
                    "id":[], 
                    "url":[], 
                    "comms_num": [], 
                    "created": [], 
                    "body":[],
                    "author":[],
                    "comments":[]}

    for i in range(len(flairs)):

        top_subreddit = subreddit.search(flairs[i], limit = numberReddits)

        count = 1

        # Feteching the required info from the subreddit posts
        for submission in top_subreddit:
            topics_dict["flair"].append(flairs[i])
            topics_dict["title"].append(submission.title)
            topics_dict["score"].append(submission.score)
            topics_dict["id"].append(submission.id)
            topics_dict["url"].append(submission.url)
            topics_dict["comms_num"].append(submission.num_comments)
            topics_dict["created"].append(submission.created)
            topics_dict["body"].append(submission.selftext)
            topics_dict["author"].append(submission.author)
            submission.comments.replace_more(limit = 0) 
            temp_comment = ''
            comment_count = 0
            for comment_iter in submission.comments:
                temp_comment+= ' ' + comment_iter.body
                comment_count+=1
                if(comment_count==50):
                    break
            topics_dict["comments"].append(temp_comment)
            # Counter to see the progress of downloading
            print("Flair count: " + str(i+1) + "  " + "Subreddit count: " + str(count) + "  Comment Count: " + str(comment_count))
            count+=1

    topics_data = pd.DataFrame(topics_dict)
    _timestamp = topics_data["created"].apply(get_date)
    topics_data = topics_data.assign(timestamp = _timestamp)
    file_name = 'reddit_flair_data.csv'
    topics_data.to_csv(file_name, index=False)    

if __name__=='__main__':
    fetch_data()