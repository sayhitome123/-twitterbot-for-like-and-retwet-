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

user = api.me()
print('Account name: ' + user.name)
def get_tweets(api,username):
    page=1
    deadend=False
    while True:
        tweets=api.list_timeline(list_id='1265742486405812225',include_rts=False) #Doing Libya politics list
        #if you want to do it for your home timeline: api.home_timeline()
        #if you want it for user do it for user api.user_timeline(username,page=page)
        Now=datetime.datetime.now()

        for tweet in tweets:
            if (Now - tweet.created_at).days < 2:
                print('------------------------')
                print('User Name: ' + tweet.user.screen_name)
                print('Date: ')
                print(tweet.created_at)
                try:
                    tweet.favorite()
                    #tweet.retweet()
                    print('Tweet Liked - ' + tweet.text)
                    time.sleep(2)
                    if tweet.retweet_count > 5:
                        tweet.retweet()
                        print('retweeted')
                        time.sleep(10)
                except tweepy.TweepError as e:
                    print(e.reason)
                except StopIteration:
                    break
            else:
                deadend= True
                return
            if not deadend:
                page=1
                time.sleep(20)


get_tweets(api, 'nbenotman')
