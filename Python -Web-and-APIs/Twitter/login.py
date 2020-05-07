from pprint import pprint

from database import Database
from twitter_utilities import get_request_token, get_oauth_verifier, get_access_token
from user import User

Database.initialise_connection(
    database='Learning',
    user='postgres',
    password='karenina',
    host='localhost',
    port=5433)
user_email = input('enter your email: \n')
user = User.load_from_db(user_email)
if user:
   print( User.load_oauth(user_email))
    # user.tweet_request_existing_user("https://api.twitter.com/1.1/search/tweets.json?q=computers+filter:images", data)

else:
    request_token = get_request_token()

    oauth_verifier = get_oauth_verifier(request_token)

    access_token = get_access_token(request_token, oauth_verifier)
    print(access_token)

    first_name = input('now first name\n')
    last_name = input('and the last name:\n')
    user = User(user_email, first_name, last_name, access_token['oauth_token'], access_token['oauth_token_secret'],
                None)
    user.save_to_db()

    # 'https://api.twitter.com/1.1/search/tweets.json?q=computers+filter:images''GET')

    tweets = user.twitter_request('https://api.twitter.com/1.1/search/tweets.json?q=computers+filter:images')
    pprint(tweets['statuses'])
    print(list(s['text'] for s in tweets['statuses']))
