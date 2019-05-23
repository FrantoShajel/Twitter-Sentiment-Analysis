# Twitter-Sentiment-Analysis
This is the code for making Sentiment Analysis in Twitter. This code uses [tweepy](http://www.tweepy.org/) library to access the Twitter API and the [TextBlob](https://textblob.readthedocs.io/en/dev/) library to perform Sentiment Analysis on each Tweet. This code shows the polarity(i.e., how positive or negative the subject in each tweet is) and subjectivity(i.e., whether it is opinion or fact) of each tweet. Also we can find the mean polarity and subjectivity of all the tweets in the particular chosen topic.

## Pre-requisites
Install the required dependencies using native pip in cmd
  - pip install tweepy
  - pip install textblob
  
## Documentations
  1. tweepy (http://www.tweepy.org/)
  2. textblob (https://textblob.readthedocs.io/en/dev/)
  
## Twitter API Setting
Go to https://developer.twitter.com/apps. Log in using your twitter account. Click 'Create App' , enter the details required and finally the app is ready to go. Go to 'Keys and Tokens' section and note the 'Consumer API keys' and 'Access Token keys'. This info will be used in the code to access the twitter API.

## Code
Open the Sentiment Analysis.py file to execute the code.
Don't forget to insert your 'Consumer API keys' and 'Access Token keys' in the code.
