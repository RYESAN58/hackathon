import requests
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json


response_API = requests.get("https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc").json()


for i in response_API:
    data = {
        "id": i['id'],
        "name": i['name'],
        "image": i['image'],
        "current_price": i['current_price'],
        "market_cap": i['market_cap'],
        "price_change_24h": i['price_change_24h'],
        }
    print(data)