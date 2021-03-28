import os
import json
import tweepy
import requests

with open('keys.json', 'r') as f:
    d = json.load(f)

auth = tweepy.OAuthHandler(d['consumer_key'], d['consumer_secret'])

redirect_url = auth.get_authorization_url()

verifier = input("get code here {} and enter > ".format(redirect_url))

auth.get_access_token(verifier)

api = tweepy.API(auth)

print(auth.access_token)
print(auth.access_token_secret)
