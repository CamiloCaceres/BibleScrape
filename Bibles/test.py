import json
from pymongo import MongoClient

client = MongoClient()
db =  client.bible


with open('BibleScrape/Bibles/jerusalen.json', 'r', encoding='utf8') as outfile:
    bible = json.load(outfile)

bible_book_number = []
for index, item in enumerate(bible.keys()):
    bible_book_number.append((str(index+1).zfill(2), item))

print(bible_book_number)