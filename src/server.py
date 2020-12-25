# has the functions that we want to implement with spotipy
# can be eventually used as a helper class, but is also currently a server for testing purposes

import spotipy
from spotipy.oauth2 import SpotifyOAuth
import config
import base64
import time
import random


sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=config.client,
                                               client_secret=config.secret,
                                               redirect_uri=config.dir,
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

# create a function that aestheticizes your playlist based on themes
#Base64 encoded JPEG image data, maximum payload size is 256 KB
def show_recent_playlists():
    # see the names of your most recent playlists
    results = sp.user_playlists(config.username)
    playlist_ids = []

    for i, item in enumerate(results['items']):
        print("%d %s" % (i, item['name']))
        if(item['owner']['id'] == user_id):
            # add all the current playlists' ids to a list for processing
            playlist_ids.append(item['uri'][item['uri'].find("list:")+5:])

    aesthetisize_playlist_covers()

def aesthetisize_playlist_covers(playlist_ids):
    # list comprehension importing images for aesthetic replacement
    neon = ["images/{}/image{}.jpg".format("neon",str(i)) for i in range(1,9)]
    pearls = ["images/{}/img{}.jpeg".format("pearls", str(i)) for i in range(1, 9)]
    abstract = ["images/{}/img{}.jpg".format("abstract", str(i)) for i in range(1, 8)]
    clouds = ["images/{}/img{}.jpeg".format("clouds", str(i)) for i in range(1, 7)]
    art = ["images/{}/art{}.jpg".format("neon", str(i)) for i in range(1, 7)]

    print("Welcome to SpotiMy")
    print("Customize your playlist covers using this quick and easy tool")
    print("The aesthetics you can choose are: neon, pearls, abstract, clouds, and art")
    user_in = input("Which aesthetic would you like? ")
    # takes the string input and converts it to the respective variable name
    images_list = eval(user_in)
    # shuffle images list so that the images aren't displayed in any particular order
    random.shuffle(images_list)

    for i in range(len(playlist_ids)-1):
        with open(images_list[i], "rb") as image_file:
            if(not images_list[i] or images_list[i] == None):
                break
            print("Updating playlist # " + str(i + 1) + ". . .")
            sp.playlist_upload_cover_image(playlist_id=playlist_ids[i],
                                       image_b64=base64.b64encode(image_file.read()))

        # allow requests to take their time
        # don't want to deal with async calls in flask for right now: future issue TODO
        time.sleep(1)

show_recent_playlists()

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