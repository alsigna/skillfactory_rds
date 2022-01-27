import requests
from pprint import pprint

response = requests.get("https://www.cbr-xml-daily.ru/daily_json.js")
print(response)
print(response.status_code)
# print(response.text)
currencies = response.json()
# pprint(currencies)
# pprint(currencies)
# print(currencies["Valute"]["CZK"]["Name"])


def currency_name(currency_id):
    url = "https://www.cbr-xml-daily.ru/daily_json.js"
    response = requests.get(url).json()["Valute"]
    for _, data in response.items():
        if data["ID"] == currency_id:
            return data["Name"]


print(currency_name("R01700J"))
