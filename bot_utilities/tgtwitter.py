__author__ = 'harsha'

import tweepy

def get_api(cfg):
  auth = tweepy.OAuthHandler(cfg['consumer_key'], cfg['consumer_secret'])
  auth.set_access_token(cfg['access_token'], cfg['access_token_secret'])
  return tweepy.API(auth)

def tweet(consumer_key, consumer_secret, access_token, access_token_secret, tweet):
  # Fill in the values noted in previous step here
  cfg = {
    "consumer_key": consumer_key,
    "consumer_secret": consumer_secret,
    "access_token": access_token,
    "access_token_secret": access_token_secret
    }

  api = get_api(cfg)
  return api.update_status(status=tweet)
  # Yes, tweet is called 'status' rather confusing