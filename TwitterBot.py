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
print('------------------------')
time.sleep(2)
Looop=2
Now=datetime.datetime.now()
while Looop <=5:

    tweets=api.list_timeline(list_id='1265742486405812225',include_rts=False) #Doing Libya politics list

#def get_tweets(api, username):
    #while True:
        #if you want to do it for your home timeline: api.home_timeline()
        #if you want it for user do it for user api.user_timeline(username,page=page)
    for tweet in tweets:
        if (Now - tweet.created_at).days < 2:
            print('User Name: ' + tweet.user.screen_name)
            print('Date: ')
            print(tweet.created_at)
            try:
                time.sleep(2)
                tweet.favorite()
                print('Tweet Liked - ' + tweet.text)
                time.sleep(3)
                print('Waiting for 07 Seconds')
                time.sleep(30)


            except tweepy.TweepError as e:
                print(e.reason)
                print('Waiting for 08 Seconds')
                time.sleep(8)


        if tweet.retweet_count > 5:
            try:
                tweet.retweet()
                print('Retweeted')
                print('Waiting for 09 Seconds')
                time.sleep(9)
                break

            except tweepy.TweepError as e:
                print(e.reason)
                print('Waiting for 10 Seconds')
                time.sleep(10)
                break
        else:
            print('Retweets are less than 5')
            time.sleep(2)
            break

    print('Waiting for 110 Seconds')
    print('------------------------')
    time.sleep(130)
