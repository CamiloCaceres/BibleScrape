import requests
from bs4 import BeautifulSoup


with open('septuaginta.html', 'r') as f:
    contents = f.read()

r = requests.get("https://www.bibliacatolica.com.br/septuaginta/exodo/1/")

soup = BeautifulSoup(contents, 'html.parser')

a = soup.find_all('a')

out = ([i['href'] for i in a])

print(out)
