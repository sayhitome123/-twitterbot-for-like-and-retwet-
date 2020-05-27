import sys
import tweepy
import datetime,time


consumer_key = '8kC67mAMcmyXNnpzgJWfIxcpI'
consumer_secret = 'YORUpiS4JuBQmsIJEdTV0HtNshN7ISVjQjD565klc97eokMp6N'
access_token = '1264192580293660681-Vhcsgp02uk3zhnAe2RmEUYR2NETDCZ'
access_token_secret = 'ntAM0po6thSsWhEnrse4SgaD4YQVxI5GJAnukqm5uWOOn'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

user = api.me()
print('Account name: ' + user.name)
def get_tweets(api,username):
    page=1
    deadend=False
    while True:
        tweets=reversed(api.list_timeline(list_id='1265742486405812225',include_rts=False)) #Doing Libya politics list
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