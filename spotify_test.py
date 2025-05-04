import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv
import os

load_dotenv()

auth_manager = SpotifyOAuth(
    client_id = os.getenv('client_id'),
    client_secret = os.getenv('client_secret'),
    redirect_uri='http://127.0.0.1:8888/callback',
    scope='user-library-read playlist-read-private playlist-read-collaborative'
)
sp = spotipy.Spotify(auth_manager=auth_manager)
# print(sp.me())
playlist = sp.playlist(playlist_id='3cduodg3v89sgtKcrecfJO', market = 'IN')
# print(playlist)


for item in playlist['tracks']['items']:
    track = item['track']
    print(f"{track['name']} by {track['artists'][0]['name']}")