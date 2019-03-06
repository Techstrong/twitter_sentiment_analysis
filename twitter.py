import tweepy
import time
import numpy
import string
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
from tweepy import Stream
import twi_api_credentials
from textblob import TextBlob
from bs4 import BeautifulSoup
from nltk.corpus import stopwords
import nltk
import Polarity
import MostUsedWords


######### TWITTER STREAM LISTENER ############
### ALLOWS US TO ACCESS AND BROADCAST TWEETS ###
#
#

class TwitterStreamer():
    """"
    Class for streaming and processing liv tweets.
    """
    def stream_tweets(self, fetched_tweets_filename, hash_tag_list):
    # This handles Twitter authentication and the connetion to the Twitter Streaming API.
        listener = StdOutListener(fetched_tweets_filename)
        auth = OAuthHandler(twi_api_credentials.consumer_key, twi_api_credentials.consumer_secret)
        auth.set_access_token(twi_api_credentials.access_token, twi_api_credentials.access_secret)

        stream = Stream(auth, listener)

        stream.filter(track=hash_tag_list)

class StdOutListener(StreamListener):
    """
    This is a basic listener class that just prints  received tweets to stdout.
    """
    def __init__(self, fetched_tweets_filename):
        self.fetched_tweets_filename = fetched_tweets_filename

    def on_data(self, data):
        try:
            print(data)
            with open(self.fetched_tweets_filename, 'a') as tf:
                tf.write(data)
            return True
        except BaseException as e:
            print("Error on_data: %s" % str(e))
            return True

    def on_error(self, status):
        print(status)

if __name__=="__main__":

    hash_tag_list = ["donald trump", "hilary clinton", "barack obama", "bernie sanders"]
    fetched_tweets_filename = "tweets.json"
    result = Twitter.cursor(Twitter.search, q=hash_tag_list)

    twitter_streamer = TwitterStreamer()
    twitter_streamer.stream_tweets(fetched_tweets_filename, hash_tag_list)

for tweet in result:
    SearchTweets = []
    SearchTweets.append(tweet['text'])
    print(SearchTweets)
