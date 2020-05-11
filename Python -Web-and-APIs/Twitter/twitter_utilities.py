import urllib.parse as urlparse

import oauth2

import constants

consumer = oauth2.Consumer(constants.CLIENT_KEY, constants.CLIENT_SECRET)


def get_request_token():
    client = oauth2.Client(consumer)
    response, content = client.request(constants.REQUEST_TOKEN_URL, 'POST')
    if response.status != 200:
        print('An error occurred getting request_token from Twitter')
    return dict(urlparse.parse_qsl(content.decode('utf-8')))


def get_oauth_verifier(request_token):
    print('Please fallow the site  in your browser')
    print(get_oauth_verifier_url(request_token))
    return input('please enter the pin\n')


def get_oauth_verifier_url(request_token):
    return '{}?oauth_token={}'.format(constants.AUTHORIZATION_URL, request_token['oauth_token'])


def get_access_token(request_token, oauth_verifier):
    token = oauth2.Token(request_token['oauth_token'], request_token['oauth_token_secret'])
    token.set_verifier(oauth_verifier)
    client = oauth2.Client(consumer, token)
    response, content = client.request(constants.ACCESS_TOKEN_URL, 'POST')
    return dict(urlparse.parse_qsl(content.decode('utf-8')))