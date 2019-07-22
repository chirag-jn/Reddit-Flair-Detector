# Reddit-Flair-Detector
Reddit Flair Detector, created as a Technical Task for Precog's Interview.

## Heroku App
https://redditflair.herokuapp.com/

## Steps to Run the App
```console
git clone https://github.com/chirag-jn/Reddit-Flair-Detector
sudo python3 -m pip install -m requirements.txt
sudo service mongodb start
python3 run.py
```

Now, go to http://localhost:5000/

## Dependencies
1. praw
2. pandas
3. dnspython
4. pymongo
5. flask
6. gunicorn
7. sklearn
8. nltk
9. numpy

## Credentials
1. Reddit Username: jnchirag
2. Reddit API Name: redditflair
3. MongoDB Name: redditflair
3. MongoDB App Username: Precog
4. All the Keys are mentioned in Scripts/redditKeys.py

## Data Fetching
1. We used the Reddit Praw API provided by Reddit for fetching subreddits of every flair.
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


## Analyzing Title, Body and Comments
1. I tested various Classification algorithms and found the accuracy in different cases using various features and group of features.
2. Classification Algorithms used:
    * Naive Bayes
    * Logistic Regression
    * Linear Support Vector Machines
    * MLP Classifier
    * Random Forest
3. I found that Random Forest provided the best results when it came to accuracy. I used a combination of the features: 
    * Title
    * Comments
4. The various accuracy results are mentioned below.


## Results

### Naive Bayes
| Feature | Accuracy (0-1) |
| --- |:---:|
| Author | 0.17154811715481172 |
| Title | 0.502092050209205 |
| Comments | 0.39748953974895396 |
| Body | 0.2175732217573222 |
| ID | 0.06694560669456066 |
| URL | 0.20920502092050208 |
| Number of Comments | 0.058577405857740586 |
| Score | 0.0794979079497908 |
| Title+Comments+URL | 0.497907949790795 |
| Title+Comments | 0.5062761506276151 |

### Logistic Regression
| Feature | Accuracy (0-1) |
| --- |:---:|
| Author | 0.17154811715481172 |
| Title | 0.5313807531380753 |
| Comments | 0.5397489539748954 |
| Body | 0.3891213389121339 |
| ID | 0.058577405857740586 |
| URL | 0.26778242677824265 |
| Number of Comments | 0.09623430962343096 |
| Score | 0.08368200836820083 |
| Title + Comments + URL | 0.6401673640167364 |
| Title + Comments | 0.6359832635983264 |

### Linear Support Vector Machines
| Feature | Accuracy (0-1) |
| --- |:---:|
| Author | 0.1799163179916318 |
| Title | 0.5774058577405857 |
| Comments | 0.5313807531380753 |
| Body | 0.3598326359832636 |
| ID | 0.07112970711297072 |
| URL | 0.2217573221757322 |
| Number of Comments | 0.07112970711297072 |
| Score | 0.07112970711297072 |
| Title+Comments+URL | 0.6276150627615062 |
| Title+Comments | 0.6150627615062761 |

### MLP Classifier
| Feature | Accuracy (0-1) |
| --- |:---:|
| Author | 0.1799163179916318 |
| Title | 0.34309623430962344 |
| Comments | 0.4100418410041841 |
| Body | 0.3389121338912134 |
| ID | 0.06694560669456066 |
| URL | 0.1799163179916318 |
| Number of Comments | 0.10460251046025104 |
| Score | 0.06694560669456066 |
| Title + Comments + URL | 0.47280334728033474 |
| Title + Comments | 0.41422594142259417 |

### Random Forest
| Feature | Accuracy (0-1) |
| --- |:---:|
| Author | 0.16736401673640167 |
| Title | 0.5146443514644351 |
| Comments | 0.5313807531380753 |
| Body | 0.41422594142259417 |
| ID | 0.058577405857740586 |
| URL | 0.1799163179916318 |
| Number of Comments | 0.100418410041841 |
| Score | 0.0794979079497908 |
| Title + Comments + URL | 0.6861924686192469 |
| Title + Comments | 0.6903765690376569 |

#### Notes
1. We won't use Body as a feature as few posts don't have any body present. So it makes our data inconsistent and hence, gives lower accuracy.

#### References
1. https://towardsdatascience.com/creating-the-twitter-sentiment-analysis-program-in-python-with-naive-bayes-classification-672e5589a7ed
2. https://towardsdatascience.com/multi-class-text-classification-model-comparison-and-selection-5eb066197568
3. https://www.reddit.com/r/India/wiki/rules#wiki_post_flairs
4. http://www.storybench.org/how-to-scrape-reddit-with-python/
5. https://colorlib.com/wp/template/login-form-v5/