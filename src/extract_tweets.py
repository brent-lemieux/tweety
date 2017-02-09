from __future__ import unicode_literals
import os
import tweepy
import pickle
import time


consumer_key = os.environ['TWITTER_KEY']
consumer_secret = os.environ['TWITTER_SECRET']
access_token = os.environ['TWITTER_AT']
access_secret = os.environ['TWITTER_TS']


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)


api = tweepy.API(auth)


def get_tweets(topics, save_file_name,num_batches=25): # num_batches * 100 is total tweets target
    tweets = set()
    # public_tweets = api.home_timeline()
    for i in xrange(num_batches):
        for topic in topics:
            try:
                print 'Loading', i+1, 'of', num_batches, 'batches of', topic, 'tweets'
                for tweet in tweepy.Cursor(api.search, q=topic).items(100):
                    if tweet.lang == 'en':
                        tweets.add(tweet.text)
                time.sleep(35)
            except:
                print 'Waiting for API to allow more calls...'
                time.sleep(60)
                pass
    pickle.dump( tweets, open( "{}.pkl".format(save_file_name), "wb" ) )
    print 'Succesfully pickled', len(tweets), 'tweets!'



if __name__ == '__main__':
    get_tweets(['chipotle', 'mcdonalds', 'starbucks'], 'food/food0209c', 100)
    # get_tweets(['noodles', 'ibotta', 'vail', 'trulia', 'otterbox', 'chaco'], 'denver/cos0207a', 100)
    # get_tweets(superb, 'sb/sb0205', 100)
    # get_tweets(['#maga'], 'data/trump_tweets_0201', 5)
    # get_tweets('economy', 'financial_tweets/econ_tweets_0124c', 50)
