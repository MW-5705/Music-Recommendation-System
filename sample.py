from bs4 import BeautifulSoup
import requests

headers = {'User-Agent' : 'Mozilla/5.0'}

url = 'https://tunebat.com/Info/Winning-Speech-Karan-Aujla-Seshnolan/3FqtduiaqnFYvBgKuc6QWQ'

req = requests.get(url=url, headers=headers, timeout=60)

print(req.text)
