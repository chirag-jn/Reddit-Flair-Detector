# Reddit-Flair-Detector
Reddit Flair Detector, created as a Technical Task for Precog's Interview.

Heroku App: redditflair.herokuapp.com

1. Install all the required packages from requirements.txt `sudo python3 -m pip install -m requirements.txt`
2. Reddit username: jnchirag
3. Reddit API Name: redditflair
4. Keys mentioned in Scripts/redditKeys.py (not public, please mail for getting access to them)
5. Scraping: http://www.storybench.org/how-to-scrape-reddit-with-python/
6. Flairs: https://www.reddit.com/r/India/wiki/rules#wiki_post_flairs

## Initial Setup
1. Install pip

## Data Fetching
1. We used the Praw API provided by Reddit for fetching subreddits of every flair.
2. The flairs which we included in our data are:
    * Political
    * Non-Political
    * AskIndia
    * Reddiquette
    * Science & Technology
    * Policy & Economy
    * Finance & Business
    * Entertainment
    * Sports
    * Food
    * Photography
    * AMA
3. 100 subreddits are collected for every flair and are collectively stored in data/reddit_flair_data.csv
4. The details of each subreddit stored are:
    * Flair Name (flair)
    * Subreddit Title (title)
    * Score (score)
    * Subreddit ID (id)
    * URL (url)
    * Number of Comments (comms_num)
    * Date created (created)
    * Body of Subreddit (body)
    * Subreddit Author (author)
    * Top Comments (comments)

## MongoDB
1. MongoDB Atlas
2. Email: chiragjn120@gmail.com
3. Project name: redditflair
4. Username: Precog
5. Password: Div@01234
6. sudo service mongodb start
