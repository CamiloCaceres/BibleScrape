import requests
from bs4 import BeautifulSoup
import json


#recibe el enlace del libro/capitulo, busca la seccion .entry y retorna una lista de todos los versiculos en ese capitulo
def get_verses(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    verses = soup.select(".entry")[0]
    p =verses.find_all('p')
    return ([i.text.lstrip('0123456789.- ') for i in p])

#recibe el enlace del libro, busca la ul .listChapter y retorna una lista de enlaces con cada capitulo
def get_chapters(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    listChapter = soup.select(".listChapter")[0]
    a = listChapter.find_all('a')
    return ([i['href'] for i in a])

#recibe url de un libro (cualquier chap), pide la lista de caps de ese libro, retorna un dict asi:
def get_book(url):
    book ={}   
    chapters = get_chapters(url)
    for num, url in enumerate(chapters, start=1):
        book[num] = get_verses(url)
    return book

def get_bible(urls):
    bible = {}
    for url in urls:
        name = url.split('/')[-3]
        bible[name] = get_book(url)
        print(f"wrote {name}")

    with open('bible.json', 'w', encoding='utf8') as outfile:
        json.dump(bible, outfile, ensure_ascii=False)






bookList = [
    "https://www.bibliacatolica.com.br/la-biblia-de-jerusalen/genesis/1/",
    "https://www.bibliacatolica.com.br/la-biblia-de-jerusalen/exodo/1/",
    "https://www.bibliacatolica.com.br/la-biblia-de-jerusalen/levitico/1/",
    "https://www.bibliacatolica.com.br/la-biblia-de-jerusalen/numeros/1/",
    "https://www.bibliacatolica.com.br/la-biblia-de-jerusalen/deuteronomio/1/",
    "https://www.bibliacatolica.com.br/la-biblia-de-jerusalen/josue/1/",
    "https://www.bibliacatolica.com.br/la-biblia-de-jerusalen/jueces/1/",
    "https://www.bibliacatolica.com.br/la-biblia-de-jerusalen/rut/1/",
    "https://www.bibliacatolica.com.br/la-biblia-de-jerusalen/i-samuel/1/",
    "https://www.bibliacatolica.com.br/la-biblia-de-jerusalen/ii-samuel/1/",
    "https://www.bibliacatolica.com.br/la-biblia-de-jerusalen/i-reyes/1/",
    "https://www.bibliacatolica.com.br/la-biblia-de-jerusalen/ii-reyes/1/",
    "https://www.bibliacatolica.com.br/la-biblia-de-jerusalen/i-cronicas/1/",
    "https://www.bibliacatolica.com.br/la-biblia-de-jerusalen/ii-cronicas/1/",
    "https://www.bibliacatolica.com.br/la-biblia-de-jerusalen/esdras/1/",
    "https://www.bibliacatolica.com.br/la-biblia-de-jerusalen/nehemias/1/",
    "https://www.bibliacatolica.com.br/la-biblia-de-jerusalen/tobias/1/",
    "https://www.bibliacatolica.com.br/la-biblia-de-jerusalen/judit/1/",
    "https://www.bibliacatolica.com.br/la-biblia-de-jerusalen/ester/1/",
    "https://www.bibliacatolica.com.br/la-biblia-de-jerusalen/job/1/",
    "https://www.bibliacatolica.com.br/la-biblia-de-jerusalen/salmos/1/",
    "https://www.bibliacatolica.com.br/la-biblia-de-jerusalen/i-macabeos/1/",
    "https://www.bibliacatolica.com.br/la-biblia-de-jerusalen/ii-macabeos/1/",
    "https://www.bibliacatolica.com.br/la-biblia-de-jerusalen/proverbios/1/",
    "https://www.bibliacatolica.com.br/la-biblia-de-jerusalen/eclesiastes/1/",
    "https://www.bibliacatolica.com.br/la-biblia-de-jerusalen/cantar/1/",
    "https://www.bibliacatolica.com.br/la-biblia-de-jerusalen/sabiduria/1/",
    "https://www.bibliacatolica.com.br/la-biblia-de-jerusalen/eclesiastico/1/",
    "https://www.bibliacatolica.com.br/la-biblia-de-jerusalen/isaias/1/",
    "https://www.bibliacatolica.com.br/la-biblia-de-jerusalen/jeremias/1/",
    "https://www.bibliacatolica.com.br/la-biblia-de-jerusalen/lamentaciones/1/",
    "https://www.bibliacatolica.com.br/la-biblia-de-jerusalen/baruc/1/",
    "https://www.bibliacatolica.com.br/la-biblia-de-jerusalen/ezequiel/1/",
    "https://www.bibliacatolica.com.br/la-biblia-de-jerusalen/daniel/1/",
    "https://www.bibliacatolica.com.br/la-biblia-de-jerusalen/oseas/1/",
    "https://www.bibliacatolica.com.br/la-biblia-de-jerusalen/joel/1/",
    "https://www.bibliacatolica.com.br/la-biblia-de-jerusalen/amos/1/",
    "https://www.bibliacatolica.com.br/la-biblia-de-jerusalen/abdias/1/",
    "https://www.bibliacatolica.com.br/la-biblia-de-jerusalen/jonas/1/",
    "https://www.bibliacatolica.com.br/la-biblia-de-jerusalen/miqueas/1/",
    "https://www.bibliacatolica.com.br/la-biblia-de-jerusalen/nahun/1/",
    "https://www.bibliacatolica.com.br/la-biblia-de-jerusalen/habacuc/1/",
    "https://www.bibliacatolica.com.br/la-biblia-de-jerusalen/sofonias/1/",
    "https://www.bibliacatolica.com.br/la-biblia-de-jerusalen/ageo/1/",
    "https://www.bibliacatolica.com.br/la-biblia-de-jerusalen/zacarias/1/",
    "https://www.bibliacatolica.com.br/la-biblia-de-jerusalen/malaquias/1/",
    "https://www.bibliacatolica.com.br/la-biblia-de-jerusalen/mateo/1/",
    "https://www.bibliacatolica.com.br/la-biblia-de-jerusalen/marcos/1/",
    "https://www.bibliacatolica.com.br/la-biblia-de-jerusalen/lucas/1/",
    "https://www.bibliacatolica.com.br/la-biblia-de-jerusalen/juan/1/",
    "https://www.bibliacatolica.com.br/la-biblia-de-jerusalen/hechos/1/",
    "https://www.bibliacatolica.com.br/la-biblia-de-jerusalen/romanos/1/",
    "https://www.bibliacatolica.com.br/la-biblia-de-jerusalen/i-corintios/1/",
    "https://www.bibliacatolica.com.br/la-biblia-de-jerusalen/ii-corintios/1/",
    "https://www.bibliacatolica.com.br/la-biblia-de-jerusalen/galatas/1/",
    "https://www.bibliacatolica.com.br/la-biblia-de-jerusalen/efesios/1/",
    "https://www.bibliacatolica.com.br/la-biblia-de-jerusalen/filipenses/1/",
    "https://www.bibliacatolica.com.br/la-biblia-de-jerusalen/colosenses/1/",
    "https://www.bibliacatolica.com.br/la-biblia-de-jerusalen/i-tesalonicenses/1/",
    "https://www.bibliacatolica.com.br/la-biblia-de-jerusalen/ii-tesalonicenses/1/",
    "https://www.bibliacatolica.com.br/la-biblia-de-jerusalen/i-timoteo/1/",
    "https://www.bibliacatolica.com.br/la-biblia-de-jerusalen/ii-timoteo/1/",
    "https://www.bibliacatolica.com.br/la-biblia-de-jerusalen/tito/1/",
    "https://www.bibliacatolica.com.br/la-biblia-de-jerusalen/filemon/1/",
    "https://www.bibliacatolica.com.br/la-biblia-de-jerusalen/hebreos/1/",
    "https://www.bibliacatolica.com.br/la-biblia-de-jerusalen/santiago/1/",
    "https://www.bibliacatolica.com.br/la-biblia-de-jerusalen/i-pedro/1/",
    "https://www.bibliacatolica.com.br/la-biblia-de-jerusalen/ii-pedro/1/",
    "https://www.bibliacatolica.com.br/la-biblia-de-jerusalen/i-juan/1/",
    "https://www.bibliacatolica.com.br/la-biblia-de-jerusalen/ii-juan/1/",
    "https://www.bibliacatolica.com.br/la-biblia-de-jerusalen/iii-juan/1/",
    "https://www.bibliacatolica.com.br/la-biblia-de-jerusalen/judas/1/",
    "https://www.bibliacatolica.com.br/la-biblia-de-jerusalen/apocalipsis/1/"
]

get_bible(bookList)
#get name = url.split('/')[-3]

# r = requests.get('https://www.bibliacatolica.com.br/la-biblia-de-jerusalen/jonas/1/')
# soup = BeautifulSoup(text, 'html.parser')
# x  = [i['href'] for i in soup.find_all('a')]
# with open('jerusalen.json', 'w', encoding='utf8') as outfile:
#     json.dump(x, outfile, ensure_ascii=False)


#usage example:
# x= get_verses('https://www.bibliacatolica.com.br/la-biblia-de-jerusalen/jonas/2/')
# print (x)




