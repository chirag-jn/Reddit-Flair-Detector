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


## Analyzing Title, Body and Comments
https://towardsdatascience.com/creating-the-twitter-sentiment-analysis-program-in-python-with-naive-bayes-classification-672e5589a7ed
punkt,stopwords, install via nltk
https://towardsdatascience.com/multi-class-text-classification-model-comparison-and-selection-5eb066197568


## Results

### Naive Bayes
| Author | 0.17154811715481172 |
|---|---|
| Title | 0.502092050209205 |
|---|---|
| Comments | 0.39748953974895396 |
|---|---|
| Body | 0.2175732217573222 |
|---|---|
| ID | 0.06694560669456066 |
|---|---|
| URL | 0.20920502092050208 |
|---|---|
| Number of Comments | 0.058577405857740586 |
|---|---|
| Score | 0.0794979079497908 |
|---|---|
| Title+Comments+URL | 0.497907949790795 |
|---|---|
| Title+Comments | 0.5062761506276151 |

### Logistic Regression
| Author | 3 |
|---|---|
| Title | 5 |
|---|---|
| Comments | 5 |
|---|---|
| Body | 5 |
|---|---|
| ID | 5 |
|---|---|
| URL | 5 |
|---|---|
| Number of Comments | 5 |
|---|---|
| Score | 5 |
|---|---|
| Title+Comments+URL | 5 |
|---|---|
| Title+Comments | 5 |

### Linear Support Vector Machine
| Author | 3 |
|---|---|
| Title | 5 |
|---|---|
| Comments | 5 |
|---|---|
| Body | 5 |
|---|---|
| ID | 5 |
|---|---|
| URL | 5 |
|---|---|
| Number of Comments | 5 |
|---|---|
| Score | 5 |
|---|---|
| Title+Comments+URL | 5 |
|---|---|
| Title+Comments | 5 |

### MLP Classifier
| Author | 3 |
|---|---|
| Title | 5 |
|---|---|
| Comments | 5 |
|---|---|
| Body | 5 |
|---|---|
| ID | 5 |
|---|---|
| URL | 5 |
|---|---|
| Number of Comments | 5 |
|---|---|
| Score | 5 |
|---|---|
| Title+Comments+URL | 5 |
|---|---|
| Title+Comments | 5 |

### Random Forest
| Author | 3 |
|---|---|
| Title | 5 |
|---|---|
| Comments | 5 |
|---|---|
| Body | 5 |
|---|---|
| ID | 5 |
|---|---|
| URL | 5 |
|---|---|
| Number of Comments | 5 |
|---|---|
| Score | 5 |
|---|---|
| Title+Comments+URL | 5 |
|---|---|
| Title+Comments | 5 |