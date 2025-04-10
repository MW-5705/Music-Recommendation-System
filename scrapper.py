from urllib.request import urlopen
from bs4 import BeautifulSoup
import os

listeners = 0

with open('My Spotify Library.csv', 'r') as data:

    data.readline()
    songs = data.readlines()
    for i in songs:
        i = i.split(',')
        i[0].replace(' ', '+')
        print(i[0].replace(' ', '+'), "   ", i[1].replace(' ', '+'))
        url = f"https://www.last.fm/music/{i[1][1:-1].replace(' ', '+')}/_/{i[0][1:-1].replace(' ', '+')}"
        print(url)
        page = urlopen(url)

        html_bytes = page.read()

        html = html_bytes.decode("utf-8")
        # print(type(html))

        with open('Data.html', 'w', encoding='utf-8') as f:
            f.write(html)
        soup = BeautifulSoup(html, 'html.parser')
        a = ((soup.find_all('abbr', class_= 'intabbr js-abbreviated-counter')))
        # print(a)
        # os.remove('Data.html')
        listener = float(a[0].text[:-1])
        listener += listener
print(listeners)

# print(html)