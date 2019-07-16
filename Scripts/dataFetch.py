#! usr/bin/env python3
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
    reddit = praw.Reddit(client_id = rkey.script,
                        client_secret = rkey.secret,
                        user_agent = rkey.name,
                        username = rkey.username,
                        passwor = rkey.password)

    subreddit = reddit.subreddit(subredditName)

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

        # if(i!=3):
        #     # print('c')
        #     continue

        top_subreddit = subreddit.search(flairs[i], limit = numberReddits)

        count = 1

        for submission in top_subreddit:
            # if(count!=39):
            #     count+=1
            #     # print('c')
            #     continue
            # print(submission.url)
            topics_dict["flair"].append(flairs[i])
            topics_dict["title"].append(submission.title)
            topics_dict["score"].append(submission.score)
            topics_dict["id"].append(submission.id)
            topics_dict["url"].append(submission.url)
            topics_dict["comms_num"].append(submission.num_comments)
            topics_dict["created"].append(submission.created)
            topics_dict["body"].append(submission.selftext)
            topics_dict["author"].append(submission.author)
            # print('break two')            
            submission.comments.replace_more(limit = 0 ) 
            # print('break one')
            temp_comment = ''
            comment_count = 0
            for comment_iter in submission.comments:
                temp_comment+= ' ' + comment_iter.body
                comment_count+=1
                # print(comment_iter.body)
                if(comment_count==50):
                    break
            # print('break the')
            topics_dict["comments"].append(temp_comment)
            print("Flair count: " + str(i+1) + "  " + "Subreddit count: " + str(count) + "  Comment Count: " + str(comment_count))
            count+=1

    topics_data = pd.DataFrame(topics_dict)
    _timestamp = topics_data["created"].apply(get_date)
    topics_data = topics_data.assign(timestamp = _timestamp)
    # print(topics_data)
    file_name = 'reddit_flair_data.csv'
    topics_data.to_csv(file_name, index=False)    

if __name__=='__main__':
    fetch_data()