import requests
import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv

load_dotenv() 
# jbv

auth_manager = SpotifyOAuth(client_id = os.getenv('client_id'), client_secret = os.getenv('client_secret'),
redirect_uri = 'http://127.0.0.1:8888/callback',
scope = "user-read-private")

s = spotipy.Spotify(auth_manager = auth_manager)

with open('My Spotify Library.csv', 'r') as f:
    a = f.readlines()
    for i in a:
        i = i.split(',')
        print (i[0], '  ', i[1], '   ', i[6])


# url = "https://api.spotify.com/v1/audio-features/7gl8XJ8EmiObfSFppTATt6"
# response = requests.get(url)
a = s.audio_analysis('3n3Ppam7vgaVa1iaRUc9Lp')

print(a)


