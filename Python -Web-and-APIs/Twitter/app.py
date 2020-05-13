from flask import Flask, render_template, session, redirect, request, url_for, g

from database import Database
from twitter_utilities import get_request_token, get_oauth_verifier_url, get_access_token
from user import User

app = Flask(__name__)
app.secret_key = '1234'

"""DECORATOR THAT SAYS THAT WHENEVER A USER VISITS OUT DOMAIN, THE FUNCTION GETS RUN"""
Database.initialise_connection(
    database='Learning',
    user='postgres',
    password='karenina',
    host='localhost',
    port=5433)


@app.before_request
def load_user_object():
    if 'screen_name' in session:
        g.user = User.load_from_db(session['screen_name'])

        # G is a global namespace for holding any data during an app context


@app.route('/')
def home_page():
    return render_template('home.html')


@app.route('/login/twitter')
def twitter_login():
    if 'screen_name' in session:
        return redirect(url_for('to_profile'))
    request_token = get_request_token()
    session['request_token'] = request_token
    return redirect(get_oauth_verifier_url(request_token))


@app.route('/logout')
def twitter_logout():
    session.clear()
    return redirect(url_for('home_page'))


@app.route('/auth/twitter')
def auth_twitter():
    oauth_verifier = request.args.get('oauth_verifier')
    access_token = get_access_token(session['request_token'], oauth_verifier)
    user = User.load_from_db(access_token['screen_name'])
    if not user:
        user = User(access_token['screen_name'], access_token['oauth_token'], access_token['oauth_token_secret'], None)
        user.save_to_db()
    session['screen_name'] = user.screen_name

    return redirect(url_for('to_profile'))


# send the user after login to the user profile
# used GINGER 2 templating language :
# we can pass variables to the render template method and use them within the HTML
@app.route('/profile')
def to_profile():
    print(g)
    return render_template('profile.html', user=g.user)


@app.route('/search')
def search():
    print("Macotaco")
    query = request.args.get('q')
    tweets = g.user.twitter_request('https://api.twitter.com/1.1/search/tweets.json?q={}'.format(query))
    text = [tweet['text'] for tweet in tweets['statuses']]
    return render_template('search.html', content=text)




# create and app and run it on local host on port 4995
app.run(port=4995)
