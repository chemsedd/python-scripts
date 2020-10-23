"""This script allows us to see the most popular movies on yts.mx
"""

import requests
from bs4 import BeautifulSoup

url = 'https://yts.mx/'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:79.0) Gecko/20100101 Firefox/79.0'
}
# Request web page
page = requests.get(url, headers=headers)
# parse
soup = BeautifulSoup(page.content, 'html.parser')
# top movies
movies = soup.find_all('a', class_='browse-movie-title')[:4]

# Popular downloads
print('Popular Downloads:')
print('------------------')
for index, movie in enumerate(movies):
    print(f'{index} > {movie.contents[0]}')
