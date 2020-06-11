import sys
import tweepy
import datetime,time
import os
from os import environ


CONSUMER_KEY = environ['CONSUMER_KEY']
CONSUMER_SECRET = environ['CONSUMER_SECRET']
ACCESS_KEY = environ['ACCESS_KEY']
ACCESS_SECRET = environ['ACCESS_SECRET']

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

muted_users = api.mutes()
friends_ids = api.friends_ids(api.me().id)

for user in muted_users:
    if user not in friends_ids:
        print(user.screen_name+ ' unfriend')
        api.destroy_mute(user.id)
        api.destroy_friendship(user.id)
        time.sleep(210)
    else:
        print('break')
        break
