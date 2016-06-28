import requests
import random
import urllib
from bs4 import BeautifulSoup
def yifi_id(max_pages):
    page = 1
    while page<=max_pages:
        url = "https://yts.to/browse-movies?page=" + str(page)
        source_code = requests.get(url)
        plain_text = source_code.text

        soup = BeautifulSoup(plain_text)

        for link in soup.findAll('a',{'class': 'browse-movie-title' }):
            href = link.get('href')
            name = link.string
            page_opener(href,name)

        page += 1

def page_opener(in_url, movie_name):
    url = in_url
    source_code = requests.get(url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text)

    for link in soup.findAll('img', {'class': 'img-responsive'} ):
        src = str(link.get('src'))
        image_downloader(src,movie_name)




def image_downloader(src, image_name):
    image_name = image_name + '.jpg'
    image = urllib.URLopener()
    image.retrieve(src, image_name)




yifi_id(1)