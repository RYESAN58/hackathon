import requests
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json

class Data:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.image = data['image']
        self.price = data['price']
        self.market_cap = data['market_cap']
        self.price_change_24h = data['price_change_24h']
    @staticmethod
    def get_all_crypto():
        all_coins = []
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
            all_coins.append(data)
        return all_coins