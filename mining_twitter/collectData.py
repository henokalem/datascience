import json
from twitterAccess import tweepy
from twitterAccess import api

def process_or_store(tweet):
    print(json.dumps(tweet))


for data in tweepy.Cursor(api.friends).items(10): ##api.home_timeline, api.user_timeline
    # Process a single status
    '''
    ##implement process_or_store function
    #process_or_store(status._json)#status._json returns timeline in json format

    #process_or_store(friend._json) #friend.json returns list of followers
    '''
    process_or_store(data._json)
