import os
import tweepy as tw
import pandas as pd
import auth
import twitter_utilities as tu

#authenticate and retrieve api object
tw_auth = auth.get()
api = tw.API(tw_auth, wait_on_rate_limit=True)

#define search term
search_words = u"#ihavecoronavirus"

#add filter to exclude retweets
filtered_search = search_words + " -filter:retweets"

#define date criteria
date_since = u"2020-01-01"

#collect tweets
#restrict results to only tweets in English
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