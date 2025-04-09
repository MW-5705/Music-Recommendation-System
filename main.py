# import requests
# import os
# import spotipy
# from spotipy.oauth2 import SpotifyOAuth, SpotifyClientCredentials
# from dotenv import load_dotenv

# load_dotenv() 

# headers = {'Authorization' : 'Bearer ' + 'BQDrGjKk684uZt7hrkUBkhhJmGozHQWbwL7WTE9q5-QD-e9XsRHIHKgE-TQQ9YTorhPuO3ODC8XRAe_GcW-gG2ZljT_oFHkmhcevW6kJ5fR7s-OYeTe9315OLEdZg9XbvPX6LyYE5yg'}

# sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
#     client_id=os.getenv('client_id'),
#     client_secret=os.getenv('client_secret'),
#     redirect_uri="http://127.0.0.1:8888/callback",
#     scope="user-read-email"  # scope needed for any user-auth flow; 'user-read-private' works too
# ))
# print(sp.me())
# track = sp.track("4uLU6hMCjMI75M1A2tKUQC")
# print(track['available_markets']) 

import os
from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyOAuth

load_dotenv()

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=os.getenv("client_id"),
    client_secret=os.getenv("client_secret"),
    redirect_uri="http://127.0.0.1:8888/callback",
    scope="user-read-email"
))

print("✅ Logged in as:", sp.me()['display_name'])

track_id = "4uLU6hMCjMI75M1A2tKUQC"
print("🎧 Getting audio analysis for:", track_id)

try:
    analysis = sp.audio_analysis(track_id)
    print("✅ Success!")
    print(analysis)
except Exception as e:
    print("❌ Failed to get audio analysis:")
    print(e)
# urn = 'spotify:track:3n3Ppam7vgaVa1iaRUc9Lp'
# url = 'http://open.spotify.com/track/6rqhFgbbKwnb9MLmUQDhG6'
# response = requests.get(url)
# print(response)
# print(sp.audio_analysis('6rqhFgbbKwnb9MLmUQDhG6'))
# response = requests.get('https://api.spotify.com/v1/audio-analysis/3n3Ppam7vgaVa1iaRUc9Lp', headers=headers)
# print(response.json())
# track_id = "11dFghVXANMlKmJXsNCbNl"  # "Cut To The Feeling" by Carly Rae Jepsen
# analysis = sp.audio_analysis(track_id)
# print(analysis)
# print(sp.audio_analysis('3n3Ppam7vgaVa1iaRUc9Lp'))

# jbv

# auth_manager = SpotifyOAuth(client_id = os.getenv('client_id'), client_secret = os.getenv('client_secret'),
# redirect_uri = 'http://127.0.0.1:8888/callback',
# scope = "user-read-private")

# s = spotipy.Spotify(auth_manager = auth_manager)

# with open('My Spotify Library.csv', 'r') as f:
#     a = f.readlines()
#     for i in a:
#         i = i.split(',')
#         print (i[0], '  ', i[1], '   ', i[6])


# # url = "https://api.spotify.com/v1/audio-features/7gl8XJ8EmiObfSFppTATt6"
# # response = requests.get(url)
# a = s.audio_analysis('3n3Ppam7vgaVa1iaRUc9Lp')
# print(catch)

# print(a)


