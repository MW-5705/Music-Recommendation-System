import spotipy
import os
from dotenv import load_dotenv

load_dotenv()

from spotipy.oauth2 import SpotifyOAuth

auth_manager = SpotifyOAuth(client_id = os.getenv('client_id'), client_secret = os.getenv('client_secret'),
redirect_uri = 'http://127.0.0.1:8888/callback',
scope = "user-read-private")


spotify = spotipy.Spotify(auth_manager=auth_manager)


a = spotify.playlist(playlist_id='37i9dQZF1EJGerVUxtH6v4')
print(a)