import tweepy
import csv
from twitter_authentication import *

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_KEY)

api = tweepy.API(auth)

public_tweets = []
ctr = 0
with open ("refugee_tweets.csv", "w", encoding='utf-8') as file:
	writer = csv.writer(file,delimiter=",",lineterminator='\n')
	writer.writerow(["tweet_text"])
	for tweets in tweepy.Cursor(api.search, q="refugees",language="en",count=100,
				    wait_on_rate_limit=True,wait_on_rate_limit_notify=True).pages(100):
		for tweet in tweets:
			content = tweet.text
			content = content.replace('\n', ' ').replace('\r','')
			public_tweets.append(content)
			writer.writerow([content])
		print (ctr)
		ctr += 1
	
	