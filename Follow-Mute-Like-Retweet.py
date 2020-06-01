import tweepy
import random
import time

consumer_key= '8kC67mAMcmyXNnpzgJWfIxcpI'
consumer_secret= 'YORUpiS4JuBQmsIJEdTV0HtNshN7ISVjQjD565klc97eokMp6N'
key= '1264192580293660681-Vhcsgp02uk3zhnAe2RmEUYR2NETDCZ'
secret= 'ntAM0po6thSsWhEnrse4SgaD4YQVxI5GJAnukqm5uWOOn'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(key,secret)
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

i=api.me()

followed = []
friends = []
liked = []

term = ["Tripoli","Libya","قرامطة","حكومة الوفاق الوطني","أبطال مصراتة","الزاوية العنقاء"]
query= random.choice(term)
search = tweepy.Cursor(api.search,q=query,result_type="recent",include_rts=False).items(400)

for tweet in search:
    print('searching....')
    if (tweet.user.followers_count < 100):
        continue
    try:
        print(tweet.text)
        time.sleep(2)
        print(tweet.favorite_count)
        print(tweet.retweet_count)
        time.sleep(3)
        tweet.favorite()
        print('tweet liked')
        time.sleep(5)
        api.create_friendship(id=tweet.user.id)
        print('Made friendship with '+tweet.user.screen_name+' now')
        print('---- user follow count')
        print(tweet.user.followers_count)
        time.sleep(3)
        api.create_mute(id=tweet.user.id)
        print(tweet.user.screen_name+' muted')
        if (tweet.retweet_count < 5):
            continue
            try:
                tweet.retweet()
                print('Tweet retweeted')
                continue
            except tweepy.TweepError as e:
                print(e.reason)
                continue

    except tweepy.TweepError as e:
        print(e.reason)
        continue

    print('waiting for 210 minutes')
    time.sleep(210)