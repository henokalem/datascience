import tweepy
from tweepy import OAuthHandler

consumer_key = 'vL7FnPpYAzB4GXmSQ4QqXLqvb'
consumer_secret = 'sKxCYwrTcwdRrKxOOf7YX4mZQTil00jvszk9wVqiTnQiWXNSGU'
access_token = '711331447-DUAFu3qLjFsq2zwY6tGGIp0uypLQ0oiXQlojZPMj'
access_secret = 'BEYtWCMhFCr0FY2n7jceQ4yDFf7HvMrNqxlBeNZq3qnUs'

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)
