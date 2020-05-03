import urllib.parse as urlparse

import oauth2

import constants

consumer = oauth2.Consumer(constants.CLIENT_KEY, constants.CLIENT_SECRET)
client = oauth2.Client(consumer)
response, content = client.request(constants.REQUEST_TOKEN_URL, 'POST')
if response.status != 200:
    print('An error occurred getting request_token from Twitter')
request_token = dict(urlparse.parse_qsl(content.decode('utf-8')))
print('Please fallow the site  in your browser')
print('{}?oauth_token={}'.format(constants.AUTHORIZATION_URL, request_token['oauth_token']))

oauth_verifier = input('please enter the pin\n')
token = oauth2.Token(request_token['oauth_token'], request_token['oauth_token_secret'])
token.set_verifier(oauth_verifier)
client = oauth2.Client(consumer, token)
response, content = client.request(constants.ACCESS_TOKEN_URL, 'POST')
access_token = dict(urlparse.parse_qsl(content.decode('utf-8')))
authorized_token = oauth2.Token(access_token['oauth_token'], access_token['oauth_token_secret'])
authorized_client = oauth2.Client(consumer,authorized_token )
