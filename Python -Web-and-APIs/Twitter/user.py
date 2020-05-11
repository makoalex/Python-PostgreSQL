import json

import oauth2

from database import GetConnectionFromPool
from twitter_utilities import consumer


class User:
    def __init__(self, screen_name, oauth_token, oauth_token_secret, id):
        self.screen_name = screen_name
        self.oauth_token = oauth_token
        self.oauth_token_secret = oauth_token_secret
        self.id = id

    def __repr__(self):
        return ' User: {}.'.format(self.screen_name)

    def save_to_db(self):
        with GetConnectionFromPool() as cursor:
            cursor.execute('Insert into Users (screen_name, oauth_token, oauth_token_secret) values '
                           '(%s, %s, %s)',
                           (self.screen_name, self.oauth_token, self.oauth_token_secret))

    @classmethod
    def load_oauth(cls, screen_name):
        with GetConnectionFromPool() as cursor:
            cursor.execute('select oauth_token, oauth_token_secret from users Where screen_name = %s', (screen_name,))
            data = cursor.fetchone()
            if data:
                print(data[0], data[1])

            def twitter_request_existing_user():
                authorized_token = oauth2.Token(data[0], data[1])
                authorized_client = oauth2.Client(consumer, authorized_token)
                response, content = authorized_client.request(
                    'https://api.twitter.com/1.1/search/tweets.json?q=computers+filter:images',
                    'GET')
                if response.status != 200:
                    print('oops')
                else:
                    tweets = json.loads(content.decode('utf-8'))
                    for tweet in tweets['statuses']:
                        print(tweet['text'])

            twitter_request_existing_user()

    def twitter_request(self, uri, verb='GET'):
        authorized_token = oauth2.Token(self.oauth_token, self.oauth_token_secret)
        authorized_client = oauth2.Client(consumer, authorized_token)

        response, content = authorized_client.request(uri, verb)
        print(response)
        if response.status != 200:
            print('An error has occurred')
        return json.loads(content.decode('utf-8'))

    @classmethod
    def load_from_db(cls, screen_name):
        with GetConnectionFromPool() as cursor:
            cursor.execute('Select* from users where screen_name = %s', (screen_name,))
            data = cursor.fetchone()
            if data:
                print(' screen_name- {}\n  Oauth Token- {}\n Oauth Token Secret {}\nID- {}'.format(
                    data[1], data[2], data[3], data[0]))
                return User(screen_name=data[1], oauth_token=data[2],
                            oauth_token_secret=data[3],
                            id=data[0])
