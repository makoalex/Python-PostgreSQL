import json

import oauth2

from database import GetConnectionFromPool
from twitter_utilities import consumer


class User:
    def __init__(self, email, first_name, last_name, oauth_token, oauth_token_secret, id):
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.oauth_token = oauth_token
        self.oauth_token_secret = oauth_token_secret
        self.id = id

    def __repr__(self):
        return ' User: {}.'.format(self.email)

    def save_to_db(self):
        with GetConnectionFromPool() as cursor:
            cursor.execute('Insert into Users (email, firstname, lastname, oauth_token, oauth_token_secret) values '
                           '(%s, %s, %s, %s, %s)',
                           (self.email, self.first_name, self.last_name, self.oauth_token, self.oauth_token_secret))

    @classmethod
    def load_oauth(cls, email):
        with GetConnectionFromPool() as cursor:
            cursor.execute('select oauth_token, oauth_token_secret from users Where email = %s', (email,))
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
    def load_from_db(cls, email):
        with GetConnectionFromPool() as cursor:
            cursor.execute('Select* from users where Email = %s', (email,))
            data = cursor.fetchone()
            if data:
                print(cls(email=data[1], first_name=data[2], last_name=data[3], oauth_token=data[4],
                          oauth_token_secret=data[5],
                          id=data[0]))
                return ' Email- {}\n First Name- {}\n Last Name- {}\n Oauth Token- {}\n Oauth Token Secret {}\nID- {}'.format(
                    data[1], data[2], data[3], data[4], data[5], data[0])
