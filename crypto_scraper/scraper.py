import requests
from prettytable import PrettyTable
from cred import api_key

class CryptoCurrency:

    base_url = "https://api.coingecko.com/api/v3/simple/price"
    prices = []
    def __init__(self, symbol):
        self.symbol = symbol
        self.add_prices_to_list()

    @property
    def complete_url(self):
        return f"{CryptoCurrency.base_url}?ids={self.symbol}&vs_currencies=usd&x_cg_demo_api_key={api_key}"

    @property
    def price(self):
        req = requests.get(self.complete_url).json()
        return float(req[self.symbol]['usd'])
    
    def add_prices_to_list(self):
        CryptoCurrency.prices.append([self.price, self.symbol])

    @staticmethod
    def prices_table():
        pt = PrettyTable(['Prices', 'Crypto Name'])
        pt.add_rows(CryptoCurrency.prices)
        return pt
    
    @staticmethod
    def show_prices():
        print(CryptoCurrency.prices_table())