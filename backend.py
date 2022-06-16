import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os
import pandas as pd
import collections
from flask import Flask
import csv
from dotenv import load_dotenv

load_dotenv()

scope = "user-top-read"
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))  


results = sp.current_user_top_artists(limit=10, offset=0, time_range='short_term')

spotPop = ['artists', 'popularity']

pop = []
for item in results['items']:
    pop.append( {'artists': item["name"][:20],'popularity': item["popularity"]} )


popsorted = (sorted(pop, key=lambda d: d['popularity'])) 


with open('topArtists.csv', 'w') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames = spotPop)
    writer.writeheader()
    writer.writerows(popsorted)


results = sp.current_user_top_artists(limit=36, offset=0, time_range='short_term')

top_genres = ['genre']

for item in results['items']:
    top_genres.extend([x[:20] for x in item['genres']])

c = collections.Counter(top_genres)

sort = dict(reversed((sorted(c.items(), key=lambda x:x[1]))))

top10 = dict(reversed(list(sort.items())[0: 10]))

top10Genres = ['genres', 'popularity']
genre = []
for k, v in top10.items():
    genre.append( {'genres': k,'popularity': v} )


with open('topGenres.csv', 'w') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames = top10Genres)
    writer.writeheader()
    writer.writerows(genre)


results = sp.current_user_top_tracks(limit=10, offset=0, time_range='short_term')

spotPop = ['tracks', 'popularity']

pop = []
for item in results['items']:
    pop.append( {'tracks': item["name"][:20],'popularity': item["popularity"]} )


popsorted = (sorted(pop, key=lambda d: d['popularity'])) 

with open('topTracks.csv', 'w') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames = spotPop)
    writer.writeheader()
    writer.writerows(popsorted)
