import tweepy
import time

auth = tweepy.OAuthHandler('X24kkVr17Tb1XhEETMXpdCrFR', '94i7VjUZqEF8QbHGjo1pVZGtfFOlLW2OAlqKNkDmXCXH5gGCGo')
auth.set_access_token('1238177705604112384-1Zq1xgii5DiNu61g3XjkTdDZVEhIc6', '7MoLXXTYmKwfTwOdvrFVNRWkBR6RrbTgzm65nr6s7XN2V')

api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

user = api.me()

search = 'SoftServe'
nrTweets = 15

for tweet in tweepy.Cursor(api.search, search).items(nrTweets):
    try:
        print('Tweet Liked')
        tweet.favorite()
        time.sleep(2)
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break

for tweet in tweepy.Cursor(api.search, search).items(nrTweets):
    try:
        print('Tweet Retweeted')
        tweet.retweet()
        time.sleep(2)
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break

