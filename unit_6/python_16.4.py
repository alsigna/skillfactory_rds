import requests
from bs4 import BeautifulSoup
from pprint import pprint

url = "https://www.kinopoisk.ru/film/42326/"
url = "https://www.kinopoisk.ru/film/321/"
response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
print(response.status_code)

page = BeautifulSoup(response.text, "html.parser")
actors = page.find_all("a", itemprop="actor")

pprint(actors)

# for i in range(len(actors)):
#     print(actors[i].text)
