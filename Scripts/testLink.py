import praw
import Scripts.redditKeys as rkey

def fetch_data(url_inp):
    reddit = praw.Reddit(client_id = rkey.script,
                        client_secret = rkey.secret,
                        user_agent = rkey.name,
                        username = rkey.username,
                        passwor = rkey.password)

    # print('url', url_inp)

    subreddit = reddit.submission(url = url_inp)

    # print('url2', subreddit)

    data = {}

    data['title'] = subreddit.title
    data['url'] = subreddit.url

    # print(data)

    return data