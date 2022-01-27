import requests
from bs4 import BeautifulSoup

url = "https://en.wikipedia.org/wiki/List_of_programming_languages"
response = requests.get(url)
print(response.status_code)

page = BeautifulSoup(response.text, "html.parser")
print(page.find("a"))

links = page.find_all("a")
print(len(links))

print([link.text for link in links[500:510]])

# Получаем все элементы с тегом 'div' и классом 'div-col'
all_blocks = page.find_all("div", class_="div-col")
# Выбираем первый по счету блок
first_block = all_blocks[0]
# Берём оттуда ссылки (ограничимся первыми десятью)
links = first_block.find_all("a")
print([link.text for link in links[:10]])
