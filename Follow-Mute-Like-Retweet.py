import tweepy
import random
import time
import os
from os import environ


CONSUMER_KEY = environ['CONSUMER_KEY']
CONSUMER_SECRET = environ['CONSUMER_SECRET']
ACCESS_KEY = environ['ACCESS_KEY']
ACCESS_SECRET = environ['ACCESS_SECRET']

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

count = 1
while count <=5:
    term = ["Tripoli","Libya","قرامطة","حكومة الوفاق الوطني","أبطال مصراتة","الزاوية العنقاء","LAAF GNA"]
    query= random.choice(term)
    search = tweepy.Cursor(api.search,q=query,result_type="recent",include_rts=False).items(1)

    for tweet in search:
        time.sleep(2)
        print('searching....')
        if (tweet.user.followers_count < 100):
            continue
        try:
            print(tweet.text)
            time.sleep(2)
            print('Likes:')
            print(tweet.retweet_count)
            time.sleep(3)
            tweet.favorite()
            print('tweet liked')

        except tweepy.TweepError as e:
            print(e.reason)

        try:
            time.sleep(5)
            api.create_friendship(id=tweet.user.id)
            print('Made friendship with ' + tweet.user.screen_name + ' now')
            time.sleep(3)
            print('---- user follow count')
            print(tweet.user.followers_count)
            time.sleep(3)
            api.create_mute(id=tweet.user.id)
            print(tweet.user.screen_name + ' muted')
        except tweepy.TweepError as e:
            print(e.reason)

        try:
            time.sleep(3)
            if (tweet.retweet_count < 5):
                continue
            try:
                tweet.retweet()
                print('Tweet retweeted')
            except tweepy.TweepError as e:
                print(e.reason)
        except tweepy.TweepError as e:
            print(e.reason)

    print('Waiting for 210 Seconds')
    time.sleep(210)

count = 1
