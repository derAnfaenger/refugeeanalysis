import tweepy

auth = tweepy.OAuthHandler("AXE7J3lFI8A9GAnhQ3EOXheOA", "lTAUGpS4g2WToSOo8NhEHQe8g2GbRBohKD6Lbdj9chrSc41K1P")
auth.set_access_token("748517935803699200-FUWCfYoWMg3m2qoBDgnFVcT6DH9rDgg", "ICVzDUWddMzrYONwweBtjPikCDhBZbkHOIcQLzz4fyZyh")

api = tweepy.API(auth)

public_tweets = api.home_timeline()
for tweet in public_tweets:
    print tweet.text