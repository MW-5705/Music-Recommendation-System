import requests

with open('My Spotify Library.csv', 'r') as f:
    a = f.readlines()
    for i in a:
        i = i.split(',')
        print (i[0], '  ', i[1], '   ', i[6])


url = "https://api.spotify.com/v1/audio-features/7gl8XJ8EmiObfSFppTATt6"
response = requests.get(url)

print(response.status_code)
