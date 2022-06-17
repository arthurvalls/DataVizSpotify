import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os
import pandas as pd
import collections
from flask import Flask
from flask import Flask, jsonify, request
from os.path import join, dirname
from dotenv import load_dotenv

app = Flask(__name__)

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

SPOTIPY_CLIENT_ID = os.environ.get("SPOTIPY_CLIENT_ID")
SPOTIPY_CLIENT_SECRET = os.environ.get("SPOTIPY_CLIENT_SECRET")
SPOTIPY_REDIRECT_URI = os.environ.get("SPOTIPY_REDIRECT_URI")
scope = "user-top-read"
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))  


def get_top_artists():
    results = sp.current_user_top_artists(limit=10, offset=0, time_range='short_term')

    unsorted_top_artists = ['artists', 'popularity']

    for item in results['items']:
        unsorted_top_artists.append( {'artists': item["name"][:20],'popularity': item["popularity"]} )


    sorted_top_artists = (sorted(unsorted_top_artists, key=lambda d: d['popularity'])) 

    return sorted_top_artists


def get_top_tracks():
    results = sp.current_user_top_tracks(limit=10, offset=0, time_range='short_term')

    unsorted_top_tracks = ['tracks', 'popularity']
    for item in results['items']:
        unsorted_top_tracks.append( {'tracks': item["name"][:20],'popularity': item["popularity"]} )


    sorted_top_tracks = (sorted(unsorted_top_tracks, key=lambda d: d['popularity'])) 

    return sorted_top_tracks

def get_top_genres():
    
    results = sp.current_user_top_artists(limit=36, offset=0, time_range='short_term')

    unsorted_top_genres = ['genre']

    for item in results['items']:
        unsorted_top_genres.extend([x[:20] for x in item['genres']])

    c = collections.Counter(unsorted_top_genres)

    counted_top_genres = dict(reversed((sorted(c.items(), key=lambda x:x[1]))))

    unsorted_counted_top_genres = dict(reversed(list(counted_top_genres.items())[0: 10]))

    sorted_top_genres = ['genres', 'popularity']
    for k, v in unsorted_counted_top_genres.items():
        sorted_top_genres.append( {'genres': k,'popularity': v} )


    return sorted_top_genres
    


@app.route('/jsons')
def get_artists():
  return jsonify(get_top_artists())

def get_tracks():
  return jsonify(get_top_tracks())

def get_genres():
  return jsonify(get_top_genres())