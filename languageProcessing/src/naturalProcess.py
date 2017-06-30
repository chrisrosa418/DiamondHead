from nltk.tokenize import sent_tokenize, word_tokenize

import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
import warnings
warnings.filterwarnings("ignore")

import tweepy
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy.streaming import StreamListener

consumer_key = 'VJJs1eylXpCAWVYa10dzNjNTn'
consumer_secret = 'L3RSnvvaRSGnt6NQsV0OodKEUiRqPvUwiI9s1XLfFMmp4iDyNN'
access_token = '878108679165411328-aMJCGOxpq1kw933ybb34jNwlF1YgXuN'
access_secret = 'AjV3lzwtd00NNlOF9b3SYW4c0k8Y6zdcBL9A8Of7IHn1g'

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)

#public_tweets = api.home_timeline()
#for tweet in public_tweets:
#    print tweet.text


class MyListener(StreamListener):
    def on_data(self, data):
        try:
            with open('python.json', 'a') as f:
                f.write(data)
                return True
        except BaseException as e:
            print("Error on_data: %s" % str(e))
        return True

    def on_error(self, status):
        print(status)
        return True


twitter_stream = Stream(auth, MyListener())
twitter_stream.filter(track=['#NBADraft'])


#example_text = 'Hello Mr. Smith, how are you doing today?  The weather is great and Python is awesome.  The sky is pinkish ' \
#               'blue, you should not eat cardboard '


#print (sent_tokenize(example_text))
#print (word_tokenize(example_text))


