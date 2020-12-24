# has the functions that we want to implement with spotipy
# can be eventually used as a helper class, but is also currently a server for testing purposes

import spotipy
from spotipy.oauth2 import SpotifyOAuth
# move to .env files eventually
from PIL import Image
import base64
import time
import random

username = "77wayghwgawa808wqf2ozfqpx"
client = "00592c0b16c943fdb2bb9de236338f4c" # enter your own here
secret = "ef48fb836cd84ef493c80d14d9636bf5" # enter your own here
redir = "http://127.0.0.1:9090" # enter your own here

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client,
                                               client_secret=secret,
                                               redirect_uri=redir,
                                               scope='user-library-read \
                                               user-library-modify \
                                               user-read-recently-played \
                                               playlist-read-private \
                                               playlist-modify-private \
                                               playlist-modify-public ugc-image-upload'))

# urn = 'spotify:artist:3jOstUTkEu2JkjvRdBA5Gu'
#
# artist = sp.artist(urn)
# print(artist)

# get user info
user_id = sp.current_user()['id']

def show_recent_tracks():
    results = sp.current_user_saved_tracks()
    for idx, item in enumerate(results['items']):
        track = item['track']
        print(idx, track['artists'][0]['name'], " – ", track['name'])

def show_recent_artists():
    for sp_range in ['short_term']:
        print("range:", sp_range)

        results = sp.current_user_top_artists(limit=20)

        for i, item in enumerate(results['items']):
            print(i, item["name"])
        print()

def show_recent_playlists():
    # see the names of your most recent playlists
    results = sp.user_playlists(username)
    playlist_ids = []
    images_list = ["images/image1.jpg","images/image2.jpg","images/image3.jpg","images/image4.jpg","images/image5.jpg", "images/image6.jpg"]
    random.shuffle(images_list)
    print(images_list)
    for i, item in enumerate(results['items']):
        print("%d %s" % (i, item['name']))
        if(item['owner']['id'] == user_id):
            # add all the current playlists' ids to a list for processing
            playlist_ids.append(item['uri'][item['uri'].find("list:")+5:])

    print(len(playlist_ids))

    for i in range(len(playlist_ids)-1):
        with open(images_list[i], "rb") as image_file:
            print("change")
            sp.playlist_upload_cover_image(playlist_id=playlist_ids[i],
                                       image_b64=base64.b64encode(image_file.read()))
        # allow requests to take their time
        # don't want to deal with async calls in flask for right now: future issue TODO
        time.sleep(1)



show_recent_playlists()
# create a function that aestheticizes your playlist based on themes
#Base64 encoded JPEG image data, maximum payload size is 256 KB


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