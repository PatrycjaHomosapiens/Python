# Zadanie 90:

import requests
from bs4 import BeautifulSoup

page = requests.get('https://allegro.pl/oferta/m-kurtka-meska-z-kapturem-przejsciowa-7580406963?bi_s=ads&bi_m=listing%3Adesktop%3Aquery&bi_c=YjUyZDViZjEtMTg3Yi00NzIxLWFkNjktMDBjZjE0MWRiMTM0AA&bi_t=ape&referrer=proxy&emission_unit_id=b87b9cfa-1e5a-43da-baca-265074e3b81a')
soup = BeautifulSoup(page.content, 'html.parser')

soup = list(soup.find(class_="_9b25eb10"))      # żeby dotrzeć do "_9b25eb10" trzeba najechać na nazwę produktu
                                # i wybrać "Zbadaj element" a następnie wyszukać klasę dla nazwy naszego produdktu
print(soup[0])

soup = BeautifulSoup(page.content, 'html.parser')
soup = soup.find(itemprop="price")
soup = soup['content']
print(soup)