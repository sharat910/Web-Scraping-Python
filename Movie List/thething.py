import sys
import site

import requests
from bs4 import BeautifulSoup
import unicodedata

def remove_accents(input_str):
    nkfd_form = unicodedata.normalize('NFKD', input_str)
    only_ascii = nkfd_form.encode('ASCII', 'ignore')
    return only_ascii



def kat_crwlr(max_pages):
    page = 1
    while page <= max_pages:
        url = 'https://kat.cr/movies/' + str(page) + '/'
        source_code = requests.get(url)
        plain_text = source_code.text

        soup = BeautifulSoup(plain_text)

        text_file = open("movie.txt", "a")

        for link in soup.findAll('a',{'class': 'cellMainLink' }):
            title = link.string
            try:
                text_file.write(str(title) + '\n')
                # if "YIFY" in str(title):
                #     text_file.write(str(title) + '\n')
            except:
                pass

        text_file.close()
        page += 1

n= int(raw_input("Enter the no. of pages : "))

kat_crwlr(n)
