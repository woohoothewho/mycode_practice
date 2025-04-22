from scraper import CryptoCurrency
import time
import os

if __name__ == '__main__':
    while True:
        symbol1 = CryptoCurrency(symbol='bitcoin')
        symbol2 = CryptoCurrency(symbol='ethereum')
        CryptoCurrency.show_prices()
        time.sleep(3)
        CryptoCurrency.prices.clear()
        os.system('clear')
        