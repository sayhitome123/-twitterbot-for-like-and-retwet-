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
    term = ["طرابلس","طبرق","بنغازي","Tripoli GNU","مصراتة","ليبيا","حكومة الوحدة الوطنية"]
    query= random.choice(term)
    search = tweepy.Cursor(api.search,q=query,result_type="recent",include_rts=False).items(1)

    for tweet in search:
        time.sleep(10)
        print('searching....')
        if (tweet.user.followers_count < 100):
            continue
        try:
            print(tweet.text)
            time.sleep(10)
            print('Likes:')
            print(tweet.retweet_count)
            time.sleep(8)
            tweet.favorite()
            print('tweet liked')

        except tweepy.TweepError as e:
            print(e.reason)

        try:
            time.sleep(15)
            api.create_friendship(id=tweet.user.id)
            print('Made friendship with ' + tweet.user.screen_name + ' now')
            time.sleep(14)
            print('---- user follow count')
            print(tweet.user.followers_count)
            time.sleep(14)
            api.create_mute(id=tweet.user.id)
            print(tweet.user.screen_name + ' muted')
        except tweepy.TweepError as e:
            print(e.reason)

        try:
            time.sleep(15)
            if (tweet.retweet_count < 5):
                continue
            try:
                tweet.retweet()
                print('Tweet retweeted')
            except tweepy.TweepError as e:
                print(e.reason)
        except tweepy.TweepError as e:
            print(e.reason)

    print('Waiting for 650 Seconds')
    time.sleep(650)

count = 1
