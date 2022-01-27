# import pandas as pd
# import requests
# from bs4 import BeautifulSoup

# url = "https://www.cbr.ru/key-indicators/"
# url = "https://www.banki.ru/banks/ratings/"

# Таблица с драгметаллами оказалась третьей по счёту
# print(pd.read_html(url)[1])


# response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
# print(response.status_code)
# soup = BeautifulSoup(response.text, "html.parser")
# all_blocks = soup.find_all("div", class_="key-indicator_content offset-md-2")
# # Данные таблицы с драгметаллами находятся в третьем блоке
# data = all_blocks[2].find("table")


# df = pd.read_html(str(data))[0]
# print(df)


from bs4 import BeautifulSoup
import pandas as pd
import requests

url = "https://www.banki.ru/banks/ratings/"
soup = BeautifulSoup(
    requests.get(url, headers={"User-Agent": "Mozilla/5.0"}).text, "html.parser"
)
all_blocks = soup.find_all("div", class_="layout-column-full")
# # Данные таблицы с драгметаллами находятся во втором блоке
data = all_blocks[2].find("table")
df = pd.read_html(str(data))[0]  # читаем html
print(df)