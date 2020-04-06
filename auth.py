import os
import tweepy as tw

def get() :
    api_key = os.environ.get('twitter_api_key')
    api_secret =  os.environ.get('twitter_api_secret')
    access_token_key =  os.environ.get('twitter_access_token_key')
    access_token_secret =  os.environ.get('twitter_access_token_secret')

    auth = tw.OAuthHandler(api_key, api_secret)
    auth.set_access_token(access_token_key, access_token_secret)

    return auth