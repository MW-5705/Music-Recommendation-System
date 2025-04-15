from bs4 import BeautifulSoup
import requests
import os
import time

listeners = 0
scrobbles = 0

def converter(text):
            if (text[-1] == 'K'):
                return float(text[:-1])*1000
            elif (text[-1] == 'M'):
                return float(text[:-1])*1000000
            else:
                return float(text[:-1])        
n = 0

with open('SpotifySongs.csv', 'r', encoding='utf-8') as data:
    data.readline()
    songs = data.readlines()
    for i in songs:
        n += 1
        i = i.split(',')
        print(i)
        print(i[0].replace(' ', '+'), "   ", i[1].replace(' ', '+'))
        song = ''
        artist = ''
        if (i[0][0] == '"' and i[0][-1] == '"'):
            song = i[0][1:-1]
            artist = i[1][1:-1]
        else:
            song = i[0]
            artist = i[1]
        url = f"https://www.last.fm/music/{artist.replace(' ', '+')}/_/{song.replace(' ', '+')}"
        print(url)
        headers = {'User-Agent' : 'Mozilla/5.0'}
        
        req = requests.get(url=url, headers=headers, timeout=10)
        soup = BeautifulSoup(req.text, 'html.parser')
        try:
            
            a = ((soup.find_all('abbr', class_= 'intabbr js-abbreviated-counter')))
            # print(a)
            # os.remove('Data.html')
            listener_text = a[0].text
            scrobble_text = a[1].text
            listener_text = listener_text.replace(',', '')
            scrobble_text = scrobble_text.replace(',', '')
            a1= converter(scrobble_text)
            a2= converter(listener_text)
            print(a1/a2)
            scrobbles += converter(scrobble_text)
            listeners += converter(listener_text)
        except:
            continue
        time.sleep(2)
        
        
print(listeners/n)
print(scrobbles/n)
popularity = (scrobbles/listeners)
print(popularity)
# print(html)

