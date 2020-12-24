# has the functions that we want to implement with spotipy
# can be eventually used as a helper class, but is also currently a server for testing purposes

import spotipy
from spotipy.oauth2 import SpotifyOAuth
client = "00592c0b16c943fdb2bb9de236338f4c" # enter your own here
secret = "ef48fb836cd84ef493c80d14d9636bf5" # enter your own here
redir = "http://127.0.0.1:9090" # enter your own here

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client,
                                               client_secret=secret,
                                               redirect_uri=redir,
                                               scope="user-library-read"))

results = sp.current_user_saved_tracks()
for idx, item in enumerate(results['items']):
    track = item['track']
    print(idx, track['artists'][0]['name'], " – ", track['name'])

# from flask import Flask, render_template, redirect, request, session, make_response,session,redirect
# import spotipy
# import spotipy.util as util
# import time
# import json
# app = Flask(__name__)
#

# API_BASE = 'https://accounts.spotify.com'
#
# # Make sure you add this to Redirect URIs in the setting of the application dashboard
# REDIRECT_URI = "http://127.0.0.1:5000/api_callback"
#
# SCOPE = 'playlist-modify-private,playlist-modify-public,user-top-read'
#
# # Set this to True for testing but you probaly want it set to False in production.
# SHOW_DIALOG = True
#
#
# # authorization-code-flow Step 1. Have your application request authorization;
# # the user logs in and authorizes access
# @app.route("/")
# def verify():
#     # Don't reuse a SpotifyOAuth object because they store token info and you could leak user tokens if you reuse a SpotifyOAuth object
#     sp_oauth = spotipy.oauth2.SpotifyOAuth(client_id = CLI_ID, client_secret = CLI_SEC, redirect_uri = REDIRECT_URI, scope = SCOPE)
#     auth_url = sp_oauth.get_authorize_url()
#     print(auth_url)
#     return redirect(auth_url)
#
# @app.route("/index")
# def index():
#     return render_template("index.html")
#
# # authorization-code-flow Step 2.
# # Have your application request refresh and access tokens;
# # Spotify returns access and refresh tokens
# @app.route("/api_callback")
# def api_callback():
#     # Don't reuse a SpotifyOAuth object because they store token info and you could leak user tokens if you reuse a SpotifyOAuth object
#     sp_oauth = spotipy.oauth2.SpotifyOAuth(client_id = CLI_ID, client_secret = CLI_SEC, redirect_uri = REDIRECT_URI, scope = SCOPE)
#     session.clear()
#     code = request.args.get('code')
#     token_info = sp_oauth.get_access_token(code)
#
#     # Saving the access token along with all other token related info
#     session["token_info"] = token_info
#
#
#     return redirect("index")
#
# # authorization-code-flow Step 3.
# # Use the access token to access the Spotify Web API;
# # Spotify returns requested data
# @app.route("/go", methods=['POST'])
# def go():
#     session['token_info'], authorized = get_token(session)
#     session.modified = True
#     if not authorized:
#         return redirect('/')
#     data = request.form
#     sp = spotipy.Spotify(auth=session.get('token_info').get('access_token'))
#     response = sp.current_user_top_tracks(limit=data['num_tracks'], time_range=data['time_range'])
#
#     # print(json.dumps(response))
#
#     return render_template("results.html", data=data)
#
# # Checks to see if token is valid and gets a new token if not
# def get_token(session):
#     token_valid = False
#     token_info = session.get("token_info", {})
#
#     # Checking if the session already has a token stored
#     if not (session.get('token_info', False)):
#         token_valid = False
#         return token_info, token_valid
#
#     # Checking if token has expired
#     now = int(time.time())
#     is_token_expired = session.get('token_info').get('expires_at') - now < 60
#
#     # Refreshing token if it has expired
#     if (is_token_expired):
#         # Don't reuse a SpotifyOAuth object because they store token info and you could leak user tokens if you reuse a SpotifyOAuth object
#         sp_oauth = spotipy.oauth2.SpotifyOAuth(client_id = CLI_ID, client_secret = CLI_SEC, redirect_uri = REDIRECT_URI, scope = SCOPE)
#         token_info = sp_oauth.refresh_access_token(session.get('token_info').get('refresh_token'))
#
#     token_valid = True
#     return token_info, token_valid
#
# if __name__ == "__main__":
#     app.run(debug=True)



# import requests
# from flask import render_template, Flask
#
# GET_ARTIST_ENDPOINT = 'https://api.spotify.com/v1/artists/{id}'
# SEARCH_ENDPOINT = 'https://api.spotify.com/v1/search'
# RELATED_ARTISTS_ENDPOINT = 'https://api.spotify.com/v1/artists/{id}/related-artists'
# TOP_TRACKS_ENDPOINT = 'https://api.spotify.com/v1/artists/{id}/top-tracks'
#
# # https://developer.spotify.com/web-api/get-artist/
# def get_artist(artist_id):
#     url = GET_ARTIST_ENDPOINT.format(id=artist_id)
#     resp = requests.get(url)
#     return resp.json()
#
#
# # https://developer.spotify.com/web-api/search-item/
# def search_by_artist_name(name):
#     myparams = {'type': 'artist'}
#     myparams['q'] = name
#     resp = requests.get(SEARCH_ENDPOINT, params=myparams)
#     return resp.json()
#
#
# # https://developer.spotify.com/web-api/get-related-artists/
# def get_related_artists(artist_id):
#     url = RELATED_ARTISTS_ENDPOINT.format(id=artist_id)
#     resp = requests.get(url)
#     return resp.json()
#
# # https://developer.spotify.com/web-api/get-artists-top-tracks/
# def get_artist_top_tracks(artist_id, country='US'):
#     url = TOP_TRACKS_ENDPOINT.format(id=artist_id)
#     myparams = {'country': country}
#     resp = requests.get(url, params=myparams)
#     return resp.json()
#
# app = Flask(__name__)
#
# @app.route('/')
# def homepage():
#     html = render_template('homepage.html')
#     return html
#
# @app.route('/search/<name>')
# def search(name):
#     data = search_by_artist_name(name)
#     api_url = data['artists']['href']
#     items = data['artists']['items']
#     html = render_template('search.html',
#                             artist_name=name,
#                             results=items,
#                             api_url=api_url)
#     return html
#
#
#
#
# @app.route('/artist/<id>')
# def artist(id):
#     artist = get_artist(id)
#
#     if artist['images']:
#         image_url = artist['images'][0]['url']
#     else:
#         image_url = 'http://placecage.com/600/400'
#
#     tracksdata = get_artist_top_tracks(id)
#     tracks = tracksdata['tracks']
#
#     artistsdata = get_related_artists(id)
#     relartists = artistsdata['artists']
#     html = render_template('artist.html',
#                             artist=artist,
#                             related_artists=relartists,
#                             image_url=image_url,
#                             tracks=tracks)
#     return html
#
#
#
# if __name__ == '__main__':
#     app.run(use_reloader=True, debug=True)