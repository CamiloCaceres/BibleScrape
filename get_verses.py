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

    with open('septuaginta.json', 'w', encoding='utf8') as outfile:
        json.dump(bible, outfile, ensure_ascii=False)

septuaginta = ['https://www.bibliacatolica.com.br/septuaginta/genesis/1/', 'https://www.bibliacatolica.com.br/septuaginta/exodo/1/', 'https://www.bibliacatolica.com.br/septuaginta/levitico/1/', 'https://www.bibliacatolica.com.br/septuaginta/numeros/1/', 'https://www.bibliacatolica.com.br/septuaginta/deuteronomio/1/', 'https://www.bibliacatolica.com.br/septuaginta/josue/1/', 'https://www.bibliacatolica.com.br/septuaginta/juizes/1/', 'https://www.bibliacatolica.com.br/septuaginta/rute/1/', 'https://www.bibliacatolica.com.br/septuaginta/i-samuel/1/', 'https://www.bibliacatolica.com.br/septuaginta/ii-samuel/1/', 'https://www.bibliacatolica.com.br/septuaginta/i-reis/1/', 'https://www.bibliacatolica.com.br/septuaginta/ii-reis/1/', 'https://www.bibliacatolica.com.br/septuaginta/i-cronicas/1/', 'https://www.bibliacatolica.com.br/septuaginta/ii-cronicas/1/', 'https://www.bibliacatolica.com.br/septuaginta/esdras/1/', 'https://www.bibliacatolica.com.br/septuaginta/neemias/1/', 'https://www.bibliacatolica.com.br/septuaginta/tobias/1/', 'https://www.bibliacatolica.com.br/septuaginta/judite/1/', 'https://www.bibliacatolica.com.br/septuaginta/ester/1/', 'https://www.bibliacatolica.com.br/septuaginta/jo/1/', 'https://www.bibliacatolica.com.br/septuaginta/salmos/1/', 'https://www.bibliacatolica.com.br/septuaginta/i-macabeus/1/', 'https://www.bibliacatolica.com.br/septuaginta/ii-macabeus/1/', 'https://www.bibliacatolica.com.br/septuaginta/proverbios/1/', 'https://www.bibliacatolica.com.br/septuaginta/eclesiastes/1/', 'https://www.bibliacatolica.com.br/septuaginta/cantico-dos-canticos/1/', 'https://www.bibliacatolica.com.br/septuaginta/sabedoria/1/', 'https://www.bibliacatolica.com.br/septuaginta/eclesiastico/1/', 'https://www.bibliacatolica.com.br/septuaginta/isaias/1/', 'https://www.bibliacatolica.com.br/septuaginta/jeremias/1/', 'https://www.bibliacatolica.com.br/septuaginta/lamentacoes/1/', 'https://www.bibliacatolica.com.br/septuaginta/baruc/1/', 'https://www.bibliacatolica.com.br/septuaginta/ezequiel/1/', 'https://www.bibliacatolica.com.br/septuaginta/daniel/1/', 'https://www.bibliacatolica.com.br/septuaginta/oseias/1/', 'https://www.bibliacatolica.com.br/septuaginta/joel/1/', 'https://www.bibliacatolica.com.br/septuaginta/amos/1/', 'https://www.bibliacatolica.com.br/septuaginta/abdias/1/', 'https://www.bibliacatolica.com.br/septuaginta/jonas/1/', 'https://www.bibliacatolica.com.br/septuaginta/miqueias/1/', 'https://www.bibliacatolica.com.br/septuaginta/naum/1/', 'https://www.bibliacatolica.com.br/septuaginta/habacuc/1/', 'https://www.bibliacatolica.com.br/septuaginta/sofonias/1/', 'https://www.bibliacatolica.com.br/septuaginta/ageu/1/', 'https://www.bibliacatolica.com.br/septuaginta/zacarias/1/', 'https://www.bibliacatolica.com.br/septuaginta/malaquias/1/', 'https://www.bibliacatolica.com.br/septuaginta/sao-mateus/1/', 'https://www.bibliacatolica.com.br/septuaginta/sao-marcos/1/', 'https://www.bibliacatolica.com.br/septuaginta/sao-lucas/1/', 'https://www.bibliacatolica.com.br/septuaginta/sao-joao/1/', 'https://www.bibliacatolica.com.br/septuaginta/atos-dos-apostolos/1/', 'https://www.bibliacatolica.com.br/septuaginta/romanos/1/', 'https://www.bibliacatolica.com.br/septuaginta/i-corintios/1/', 'https://www.bibliacatolica.com.br/septuaginta/ii-corintios/1/', 'https://www.bibliacatolica.com.br/septuaginta/galatas/1/', 'https://www.bibliacatolica.com.br/septuaginta/efesios/1/', 'https://www.bibliacatolica.com.br/septuaginta/filipenses/1/', 'https://www.bibliacatolica.com.br/septuaginta/colossenses/1/', 'https://www.bibliacatolica.com.br/septuaginta/i-tessalonicenses/1/', 'https://www.bibliacatolica.com.br/septuaginta/ii-tessalonicenses/1/', 'https://www.bibliacatolica.com.br/septuaginta/i-timoteo/1/', 'https://www.bibliacatolica.com.br/septuaginta/ii-timoteo/1/', 'https://www.bibliacatolica.com.br/septuaginta/tito/1/', 'https://www.bibliacatolica.com.br/septuaginta/filemon/1/', 'https://www.bibliacatolica.com.br/septuaginta/hebreus/1/', 'https://www.bibliacatolica.com.br/septuaginta/sao-tiago/1/', 'https://www.bibliacatolica.com.br/septuaginta/i-sao-pedro/1/', 'https://www.bibliacatolica.com.br/septuaginta/ii-sao-pedro/1/', 'https://www.bibliacatolica.com.br/septuaginta/i-sao-joao/1/', 'https://www.bibliacatolica.com.br/septuaginta/ii-sao-joao/1/', 'https://www.bibliacatolica.com.br/septuaginta/iii-sao-joao/1/', 'https://www.bibliacatolica.com.br/septuaginta/sao-judas/1/', 'https://www.bibliacatolica.com.br/septuaginta/apocalipse/1/']


get_bible(septuaginta)




