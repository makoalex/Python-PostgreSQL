import os


CLIENT_KEY = os.environ['TWITTER_CLIENT_KEY']
CLIENT_SECRET = os.environ['TWITTER_CLIENT_SECRET']

REQUEST_TOKEN_URL = 'https://api.twitter.com/oauth/request_token'
ACCESS_TOKEN_URL = 'https://api.twitter.com/oauth/access_token'
AUTHORIZATION_URL = 'https://api.twitter.com/oauth/authorize'
