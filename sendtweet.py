import os
import tweepy as tw
import auth

tw_auth = auth.get()
api = tw.API(tw_auth, wait_on_rate_limit=True)

#post a tweet from python
api.update_status("I'm tweeting from #python - testing code again after moving a few things around")