import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv
import os
from bs4 import BeautifulSoup
import requests
import time
import csv
import numpy as np
from google import  genai
load_dotenv()

client = genai.Client(api_key=os.getenv('api_key'), http_options={'api_version': 'v1alpha'})

id = input('Enter a spotify playlist id: ')


listeners = 0
scrobbles = 0
bpm = 0
n = 0

genres = {"acoustic": 0, "classical":0, "dance":0,"electronic":0, "hiphop" : 0, "instrumental" : 0, "jazz" : 0,"pop" : 0, "rock" : 0 }
heard = []
new_data = []
def converter(text):
            if (text[-1] == 'K'):
                return float(text[:-1])*1000
            elif (text[-1] == 'M'):
                return float(text[:-1])*1000000
            else:
                return float(text[:-1])        

def euclidean(p1, p2):
    return np.sqrt(np.sum((p1-p2)**2))


auth_manager = SpotifyOAuth(
    client_id = os.getenv('client_id'),
    client_secret = os.getenv('client_secret'),
    redirect_uri='http://127.0.0.1:8888/callback',
    scope='user-library-read playlist-read-private playlist-read-collaborative'
)
sp = spotipy.Spotify(auth_manager=auth_manager)

try:
    playlist = sp.playlist(playlist_id=id, market = 'IN')
except Exception as e:
    print(F'Facing some errors as of now {e}')
    exit()


for item in playlist['tracks']['items']:
    track = item['track']
    print(f"{track['name']} by {track['artists'][0]['name']}")
    song = track['name']
    artist = track['artists'][0]['name']
    url = f"https://www.last.fm/music/{artist.replace(' ', '+')}/_/{song.replace(' ', '+')}"
    print(url)
    try:
        response = client.models.generate_content(
            model = "gemini-2.0-flash-lite",
            contents = f"what is genre of {song} by {artist} in one word and bpm only digits separated with a comma in the form genre, bpm? strictly out of these acoustic,  classical,  dance  electronic  hiphop  instrumental  jazz  pop  rock"
        )
        headers = {'User-Agent' : 'Mozilla/5.0'}
        
        req = requests.get(url=url, headers=headers, timeout=10)
        soup = BeautifulSoup(req.text, 'html.parser')
        abbr = ((soup.find_all('abbr', class_= 'intabbr js-abbreviated-counter')))
        listener_text = abbr[0].text
        scrobble_text = abbr[1].text
        listener_text = listener_text.replace(',', '')
        scrobble_text = scrobble_text.replace(',', '')
        scrobbles_song= converter(scrobble_text)
        listeners_song= converter(listener_text)
        bpm_song = int(response.text.split(',')[1])
        bpm += bpm_song
        genre = response.text.split(',')[0].lower().replace('-', '')
        genres[genre] += 1
        scrobbles += scrobbles_song
        listeners += listeners_song
        traits = [song,artist,scrobbles_song/listeners_song,bpm_song,genre]
        heard.append(song)
        new_data.append(traits)
        print(traits)
        n += 1
    except:
        continue
    time.sleep(5)

final = [genres[key] for key in genres]
mode_genre = max(final)

if listeners == 0 or n == 0:
    popularity = 0
else:
    popularity = (scrobbles/listeners)/n
    
bpm = bpm/n
playlist_average = np.array([bpm, popularity, mode_genre])

songs = []
    
with open("spotifysongs_with_genre.csv", "r", encoding='utf-8') as dataset:
    csv_reader = csv.DictReader(dataset)
    next(csv_reader)
    for song in csv_reader:
        songs.append([float(song['Tempo']), float(song['Popularity']), genres[song['Genre'].lower().replace('-', '')], song['SongName'], song['ArtistName']])
    
neighbours = []

for song in songs:
    point = np.array([song[0], song[1], song[2]])
    dist = euclidean(playlist_average, point)
    neighbours.append([dist, song[3], song[4]])

neighbours.sort(key = lambda x:x[0])

print('Recommended songs: ')
k = 5
i = k
j = 0

while (i > 0 and j < len(neighbours)):
    if (neighbours[j][1] not in heard):
        print(f"{neighbours[j][1]} by {neighbours[j][2]}")
        i-=1
    j+=1
with open('spotifysongs_with_genre.csv', 'a', newline='') as dataset:
    dataset_writer = csv.writer(dataset)
    dataset_writer.writerows(new_data)