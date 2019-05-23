# -*- coding: utf-8 -*-
"""
Created on Thu May 23 18:56:33 2019

@author: Frash
"""

import tweepy
from textblob import TextBlob

api_key = '*API KEY from TWITTER API'                           #Enter the API KEY from your Twitter app
api_secret_key = 'API SECRET KEY from TWITTER API'              #Enter the API SECRET KEY from your Twitter app

access_token = 'ACCESS TOKEN from TWITTER API'                  #Enter the ACCESS TOKEN from your Twitter app
access_token_secret = 'ACCESS TOKEN SECRET from TWITTER API'    #Enter the ACCESS TOKEN SECRET from your Twitter app

auth = tweepy.OAuthHandler(api_key, api_secret_key)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

required_tweets = api.search('Fun')

polar = 0
subj = 0

for tweet in required_tweets:
    print (tweet.text)                          #Prints the text of each tweet
    analysis = TextBlob(tweet.text)
    print (analysis.sentiment)                  #Prints the polarity and subjectivity of each tweet
    polar += analysis.sentiment.polarity
    subj += analysis.sentiment.subjectivity

total_tweets = len(required_tweets)

polarity = polar/total_tweets
subjectivity = subj/total_tweets
    
print("\n\n")
print("Number of Tweets = ", total_tweets)      #Prints the total number of tweets obtained from search
print("Polarity = ",polarity)                   #Prints the mean polarity of the tweets
print("Subjectivity = ",subjectivity)           #Prints the mean subjectivity of the tweets
