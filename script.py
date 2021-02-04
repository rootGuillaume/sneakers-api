import requests
from bs4 import BeautifulSoup

url = 'https://stockx.com/fr-fr/new-releases/sneakers'
headers = {'user-agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:84.0) Gecko/20100101 Firefox/84.0'}

r = requests.get(url, headers=headers)
code = r.status_code

soup = BeautifulSoup(r, 'lxml')

print(soup)
