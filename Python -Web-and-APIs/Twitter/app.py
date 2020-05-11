from flask import Flask, render_template, session, redirect, request

from twitter_utilities import get_request_token, get_oauth_verifier_url, get_access_token
from user import User
from database import  Database

app = Flask(__name__)
app.secret_key = '1234'

"""DECORATOR THAT SAYS THAT WHENEVER A USER VISITS OUT DOMAIN, THE FUNCTION GETS RUN"""
Database.initialise_connection(
    database='Learning',
    user='postgres',
    password='karenina',
    host='localhost',
    port=5433)


@app.route('/')
def home_page():
    return render_template('home.html')


@app.route('/login/twitter')
def twitter_login():
    request_token = get_request_token()
    session['request_token'] = request_token
    return redirect(get_oauth_verifier_url(request_token))


@app.route('/auth/twitter')
def auth_twitter():
    oauth_verifier = request.args.get('oauth_verifier')
    access_token = get_access_token(session['request_token'], oauth_verifier)
    user = User.load_from_db(access_token['screen_name'])
    if not user:
        user = User(access_token['screen_name'], access_token['oauth_token'], access_token['oauth_token_secret'], None)
        user.save_to_db()
        session['screen_name'] = user.screen_name
    return user.screen_name


# create and app and run it on local host on port 4995
app.run(port=4995)
