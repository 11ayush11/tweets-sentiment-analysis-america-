from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import json
import time
from urllib.request import  urlopen
import http.cookiejar
import time
import pyexcel as p
from textblob import TextBlob

access_token = "xxxxxxx"
access_token_secret	= "xxxxxxxxxx"
consumer_key = "xxxxxxxxxxxxx"
consumer_secret = "xxxxxxxxxxxxxxxxxx"
class StdOutListener(StreamListener):

    def on_status(self, status):
        a = []

        description = status.user.description
        loc = status.user.location
        a.append(loc)
        text = status.text
        print(text)
        a.append((text))
        coords = status.coordinates
        a.append(coords)
        lang = status.lang
        a.append(lang)
        geo = status.geo
        a.append((geo))
        withheld_in_countries = status.place
        print (withheld_in_countries)
        name = status.user.screen_name
        a.append((name))
        user_created = status.user.created_at
        a.append((user_created))
        followers = status.user.followers_count
        id_str = status.id_str
        created = status.created_at
        a.append(created)
        # print (created)
        retweets = status.retweet_count
        a.append((retweets))
        bg_color = status.user.profile_background_color
        blob = TextBlob(text)
        sent = blob.sentiment
        a.append(sent.polarity)
        a.append(sent.subjectivity)
        arr.append(a)
        sheet = p.Sheet(arr)
        sheet.save_as("gst1.csv")

        return True


if __name__ == '__main__':

    #This handles Twitter authetification and the connection to Twitter Streaming API
    arr = []
    l = StdOutListener()


    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

    #This line filter Twitter Streams to capture data by the keywords: 'python', 'javascript', 'ruby'
    stream.filter(track=['DONALD','HILLARY','SANDRO'])
    
    
