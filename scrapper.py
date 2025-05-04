from bs4 import BeautifulSoup
import requests
import os
import time
import csv
from dotenv import load_dotenv
import numpy as np
from google import  genai
load_dotenv()

client = genai.Client(api_key=os.getenv('api_key'), http_options={'api_version': 'v1alpha'})



listeners = 0
scrobbles = 0
bpm = 0
n = 0

genres = {"acoustic": 0, "classical":0, "dance":0,"electronic":0, "hiphop" : 0, "instrumental" : 0, "jazz" : 0,"pop" : 0, "rock" : 0 }

def converter(text):
            if (text[-1] == 'K'):
                return float(text[:-1])*1000
            elif (text[-1] == 'M'):
                return float(text[:-1])*1000000
            else:
                return float(text[:-1])        
def euclidean(p1, p2):
    return np.sqrt(np.sum((p1-p2)**2))



with open('My Spotify Library (1).csv', 'r', encoding='utf-8') as data:
    data.readline()
    songs = data.readlines()
    with open('playlist.csv', 'w', encoding='utf-8') as playlist:
        playlist.write('Song, ArtistName, Popularity, Tempo, Genre\n')
        writer = csv.writer(playlist)
        for i in songs:
            n += 1
            i = i.split(',')
            # print(i)
            # print(i[0].replace(' ', '+'), "   ", i[1].replace(' ', '+'))
            song = ''
            artist = ''
            if (i[0][0] == '"' and i[0][-1] == '"'):
                song = i[0][1:-1]
                artist = i[1][1:-1]
            else:
                song = i[0]
                artist = i[1]
            url = f"https://www.last.fm/music/{artist.replace(' ', '+')}/_/{song.replace(' ', '+')}"
            response = client.models.generate_content(
                model = "gemini-2.0-flash-lite",
                contents = f"what is genre of {song} by {artist} in one word and bpm only digits separated with a comma in the form genre, bpm? out of these acoustic  classical  dance  electronic  hiphop  instrumental  jazz  pop  rock"
            )

            # print(song, ' : ', response.text)
            # print(url)
            headers = {'User-Agent' : 'Mozilla/5.0'}
            
            req = requests.get(url=url, headers=headers, timeout=10)
            soup = BeautifulSoup(req.text, 'html.parser')
            try:
                
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
                traits = [song,artist,scrobbles_song/listeners_song,int(response.text.split(',')[1]),response.text.split(',')[0]]
                print(traits)
                writer.writerow(traits)
            except:
                continue
            time.sleep(2)

# popularity = 0
# n = 0
# with open('playlist.csv', 'r', encoding='utf-8') as  playlist:
#     playlist_reader = csv.reader(playlist)
#     next(playlist_reader)
#     for song in playlist_reader:
#         # print(song)
#         bpm += int(song[3])
#         popularity += float(song[2])
#         n = n+1
#         genres[song[4].lower().replace('-', '')] += 1

final = [genres[key] for key in genres]
mode_genre = max(final)

if listeners == 0 or n == 0:
    popularity = 0
else:
    popularity = (scrobbles/listeners)/n
# popularity = popularity/n
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

k = 5

print(neighbours[:k])

# print(songs)
# print(genres)


