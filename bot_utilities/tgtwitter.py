__author__ = 'harsha'

import tweepy

def get_api(cfg):
    auth = tweepy.OAuthHandler(cfg['consumer_key'], cfg['consumer_secret'])
    auth.set_access_token(cfg['access_token'], cfg['access_token_secret'])
    return tweepy.API(auth)

def tweet(cfg, tweet_status):
    api = get_api(cfg)
    return api.update_status(status=tweet_status)

'''
## Testing
base_url = "https://api.telegram.org/bot"
auth_file_name = "../bots/doloresBot.auth"
auth_file = open(auth_file_name, 'r')
auth_token = auth_file.readline()
consumer_key = auth_file.readline()
consumer_secret = auth_file.readline()
access_token = auth_file.readline()
access_token_secret = auth_file.readline()
auth_file.close()

# Remove the newline at end of file.
auth_token = auth_token[:-1]
consumer_key = consumer_key[:-1]
print(consumer_key)
consumer_secret = consumer_secret[:-1]
print(consumer_secret)
access_token = access_token[:-1]
print(access_token)
access_token_secret = access_token_secret[:-1]
print(access_token_secret)

cfg = {
    "consumer_key": consumer_key,
    "consumer_secret": consumer_secret,
    "access_token": access_token,
    "access_token_secret": access_token_secret
}

status = tweet(cfg, "Tweepy Test")
'''