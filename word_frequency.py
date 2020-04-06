import os
import tweepy as tw
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import itertools
import collections
import nltk
from nltk.corpus import stopwords
import networkx
import warnings
import auth
import twitter_utilities as tu

warnings.filterwarnings("ignore")

#use Seaborn to style results
sns.set(font_scale=1.5)
sns.set_style("whitegrid")

#authenticate and return api object
tw_auth = auth.get()
api = tw.API(tw_auth, wait_on_rate_limit=True)

#define search term criteria
search_words = u"#coronavirus"

#append filter to eliminate retweets
filtered_search = search_words + " -filter:retweets"

#define date criteria
date_since = u"2020-01-01"

#collect tweets
#limit to English only
#limit results to 50
tweets = tw.Cursor(api.search,
    q=filtered_search,
    lang=u"en",
    since=date_since).items(50)

#interate and collect location data
#urls are stripped and made lower case
user_locs = [[tweet.user.screen_name, tweet.user.location, tu.remove_url(tweet.text.lower())] for tweet in tweets]

#use Pandas to contain results
user_tweet_loc = pd.DataFrame(data=user_locs,
    columns=['user', "location", 'tweet'])

#print results
print(user_tweet_loc)