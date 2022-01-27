import requests
from bs4 import BeautifulSoup

url = "https://nplus1.ru/news/2019/06/04/slothbot"
response = requests.get(url)

# Теперь создадим объект BeautifulSoup, указывая html парсер
page = BeautifulSoup(response.text, "html.parser")

# Всё готово, чтобы получать данные из страницы
# Для начала получим title, отображающийся на закладках браузера
print(page.title)

# Мы получили тэг. Чтобы достать из него текст, вызовем атрибут text
print(page.title.text)

print(page.find("h1").text)
print(page.find("time").text)


def wiki_header(url):
    response = requests.get(url)
    page = BeautifulSoup(response.text, "html.parser")
    return page.find("h1").text


print(wiki_header("https://en.wikipedia.org/wiki/Operating_system"))
