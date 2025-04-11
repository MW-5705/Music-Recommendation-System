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
            

with open('My Youtube Music Library.csv', 'r') as data:
    data.readline()
    songs = data.readlines()
    for i in songs:
        i = i.split(',')
        i[0] = i[0].split('-')
        i[0][1] = i[0][1].strip()
        i[0][0] = i[0][0].replace(',', ' ')
        print(i[0][0].replace(' ', '+'), "   ", i[0][1].replace(' ', '+'))
        url = f"https://www.last.fm/music/{i[1][1:-1].replace(' ', '+')}/_/{i[0][1:-1].replace(' ', '+')}"
        print(url)
        headers = {'User-Agent' : 'Mozilla/5.0'}
        
        req = requests.get(url=url, headers=headers, timeout=10)
        soup = BeautifulSoup(req.text, 'html.parser')
        a = ((soup.find_all('abbr', class_= 'intabbr js-abbreviated-counter')))
        # print(a)
        # os.remove('Data.html')
        listener_text = a[0].text
        scrobble_text = a[1].text
        listener_text = listener_text.replace(',', '')
        scrobble_text = scrobble_text.replace(',', '')
        scrobbles += converter(scrobble_text)
        listeners += converter(listener_text)
        time.sleep(2)
        
        
print(listeners)
print(scrobbles)

# print(html)

