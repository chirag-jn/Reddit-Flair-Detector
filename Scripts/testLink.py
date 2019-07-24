import praw
import Scripts.redditKeys as rkey

reddit = praw.Reddit(client_id = rkey.script,
                    client_secret = rkey.secret,
                    user_agent = rkey.name,
                    username = rkey.username,
                    passwor = rkey.password)

def fetch_data(url_inp):
	# Loading the Input URL and fetching data from the same
    global reddit

    subreddit = reddit.submission(url = url_inp)

    data = {}

    data["flair"] = (subreddit.flair)
    data["title"] = (subreddit.title)
    data["score"] = (subreddit.score)
    data["id"] = (subreddit.id)
    data["url"] = (subreddit.url)
    data["comms_num"] = (subreddit.num_comments)
    data["created"] = (subreddit.created)
    data['body'] = (subreddit.selftext)
    data["author"] = (subreddit.author)
    subreddit.comments.replace_more(limit = 0) 
    temp_comment = ''
    comment_count = 0
    comment_arr = []
    for comment_iter in subreddit.comments:
        temp_comment+= ' ' + comment_iter.body
        comment_count+=1
        comment_arr.append(comment_iter.body)
        if(comment_count==50):
            break
    data["comments"] = temp_comment
    data['comment_arr'] = comment_arr
    return data