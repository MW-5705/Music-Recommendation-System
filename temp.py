import requests
from urllib.request import urlopen, Request

from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'Referer': 'https://songbpm.com/'
}

req = Request("https://songbpm.com/@prateek-kuhad/co2-zeR0aNC_Nn", headers=headers)
page = urlopen(req)

html_bytes = page.read()
html = html_bytes.decode("utf-8")
with open('abc.html', 'w', encoding='utf-8') as f:
    f.write(html)

# mt-1 text-3xl font-semibold text-card-foreground