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

    with open('vulgata.json', 'w', encoding='utf8') as outfile:
        json.dump(bible, outfile, ensure_ascii=False)

vulgata = ['https://www.bibliacatolica.com.br/vulgata-latina/liber-genesis/1/', 'https://www.bibliacatolica.com.br/vulgata-latina/liber-exodus/1/', 'https://www.bibliacatolica.com.br/vulgata-latina/liber-leviticus/1/', 'https://www.bibliacatolica.com.br/vulgata-latina/liber-numeri/1/', 'https://www.bibliacatolica.com.br/vulgata-latina/liber-deuteronomii/1/', 'https://www.bibliacatolica.com.br/vulgata-latina/liber-iosue/1/', 'https://www.bibliacatolica.com.br/vulgata-latina/liber-iudicum/1/', 'https://www.bibliacatolica.com.br/vulgata-latina/liber-ruth/1/', 'https://www.bibliacatolica.com.br/vulgata-latina/liber-i-samuelis/1/', 'https://www.bibliacatolica.com.br/vulgata-latina/liber-ii-samuelis/1/', 'https://www.bibliacatolica.com.br/vulgata-latina/liber-i-regum/1/', 'https://www.bibliacatolica.com.br/vulgata-latina/liber-ii-regum/1/', 'https://www.bibliacatolica.com.br/vulgata-latina/liber-i-paralipomenon/1/', 'https://www.bibliacatolica.com.br/vulgata-latina/liber-ii-paralipomenon/1/', 'https://www.bibliacatolica.com.br/vulgata-latina/liber-esdrae/1/', 'https://www.bibliacatolica.com.br/vulgata-latina/liber-nehemiae/1/', 'https://www.bibliacatolica.com.br/vulgata-latina/liber-thobis/1/', 'https://www.bibliacatolica.com.br/vulgata-latina/liber-iudith/1/', 'https://www.bibliacatolica.com.br/vulgata-latina/liber-esther/1/', 'https://www.bibliacatolica.com.br/vulgata-latina/liber-iob/1/', 'https://www.bibliacatolica.com.br/vulgata-latina/liber-psalmorum/1/', 'https://www.bibliacatolica.com.br/vulgata-latina/liber-i-maccabaeorum/1/', 'https://www.bibliacatolica.com.br/vulgata-latina/liber-ii-maccabaeorum/1/', 'https://www.bibliacatolica.com.br/vulgata-latina/liber-proverbiorum/1/', 'https://www.bibliacatolica.com.br/vulgata-latina/liber-ecclesiastes/1/', 'https://www.bibliacatolica.com.br/vulgata-latina/canticum-canticorum/1/', 'https://www.bibliacatolica.com.br/vulgata-latina/liber-sapientiae/1/', 'https://www.bibliacatolica.com.br/vulgata-latina/liber-ecclesiasticus/1/', 'https://www.bibliacatolica.com.br/vulgata-latina/liber-isaiae/1/', 'https://www.bibliacatolica.com.br/vulgata-latina/liber-ieremiae/1/', 'https://www.bibliacatolica.com.br/vulgata-latina/lamentationes/1/', 'https://www.bibliacatolica.com.br/vulgata-latina/liber-baruch/1/', 'https://www.bibliacatolica.com.br/vulgata-latina/prophetia-ezechielis/1/', 'https://www.bibliacatolica.com.br/vulgata-latina/prophetia-danielis/1/', 'https://www.bibliacatolica.com.br/vulgata-latina/prophetia-osee/1/', 'https://www.bibliacatolica.com.br/vulgata-latina/prophetia-ioel/1/', 'https://www.bibliacatolica.com.br/vulgata-latina/prophetia-amos/1/', 'https://www.bibliacatolica.com.br/vulgata-latina/prophetia-abdiae/1/', 'https://www.bibliacatolica.com.br/vulgata-latina/prophetia-ionae/1/', 'https://www.bibliacatolica.com.br/vulgata-latina/prophetia-michaeae/1/', 'https://www.bibliacatolica.com.br/vulgata-latina/prophetia-nahum/1/', 'https://www.bibliacatolica.com.br/vulgata-latina/prophetia-habacuc/1/', 'https://www.bibliacatolica.com.br/vulgata-latina/prophetia-sophoniae/1/', 'https://www.bibliacatolica.com.br/vulgata-latina/prophetia-aggaei/1/', 'https://www.bibliacatolica.com.br/vulgata-latina/prophetia-zachariae/1/', 'https://www.bibliacatolica.com.br/vulgata-latina/prophetia-malachiae/1/', 'https://www.bibliacatolica.com.br/vulgata-latina/evangelium-secundum-matthaeum/1/', 'https://www.bibliacatolica.com.br/vulgata-latina/evangelium-secundum-marcum/1/', 'https://www.bibliacatolica.com.br/vulgata-latina/evangelium-secundum-lucam/1/', 'https://www.bibliacatolica.com.br/vulgata-latina/evangelium-secundum-ioannem/1/', 'https://www.bibliacatolica.com.br/vulgata-latina/actus-apostolorum/1/', 'https://www.bibliacatolica.com.br/vulgata-latina/epistula-ad-romanos/1/', 'https://www.bibliacatolica.com.br/vulgata-latina/epistula-i-ad-corinthios/1/', 'https://www.bibliacatolica.com.br/vulgata-latina/epistula-ii-ad-corinthios/1/', 'https://www.bibliacatolica.com.br/vulgata-latina/epistula-ad-galatas/1/', 'https://www.bibliacatolica.com.br/vulgata-latina/epistula-ad-ephesios/1/', 'https://www.bibliacatolica.com.br/vulgata-latina/epistula-ad-philippenses/1/', 'https://www.bibliacatolica.com.br/vulgata-latina/epistula-ad-colossenses/1/', 'https://www.bibliacatolica.com.br/vulgata-latina/epistula-i-ad-thessalonicenses/1/', 'https://www.bibliacatolica.com.br/vulgata-latina/epistula-ii-ad-thessalonicenses/1/', 'https://www.bibliacatolica.com.br/vulgata-latina/epistula-i-ad-timotheum/1/', 'https://www.bibliacatolica.com.br/vulgata-latina/epistula-ii-ad-timotheum/1/', 'https://www.bibliacatolica.com.br/vulgata-latina/epistula-ad-titum/1/', 'https://www.bibliacatolica.com.br/vulgata-latina/epistulam-ad-philemonem/1/', 'https://www.bibliacatolica.com.br/vulgata-latina/epistula-ad-hebraeos/1/', 'https://www.bibliacatolica.com.br/vulgata-latina/epistula-iacobi/1/', 'https://www.bibliacatolica.com.br/vulgata-latina/epistula-i-petri/1/', 'https://www.bibliacatolica.com.br/vulgata-latina/epistula-ii-petri/1/', 'https://www.bibliacatolica.com.br/vulgata-latina/epistula-i-ioannis/1/', 'https://www.bibliacatolica.com.br/vulgata-latina/epistula-ii-ioannis/1/', 'https://www.bibliacatolica.com.br/vulgata-latina/epistula-iii-ioannis/1/', 'https://www.bibliacatolica.com.br/vulgata-latina/epistula-iudae/1/', 'https://www.bibliacatolica.com.br/vulgata-latina/apocalypsis-ioannis/1/']


get_bible(vulgata)




