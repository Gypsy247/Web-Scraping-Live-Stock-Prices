import json
import requests
from bs4 import BeautifulSoup

monitor_stocks = [
    'AAPL',
    'MSFT',
    'GOOGL',
    'TSM',
    'NVDA',
    'TCEHY',
    'META',
    'NFLX',
    'ASML',
    'BABA',
]
stock_data = []
user_agent = 'paste the user agent here'


def fetchStocks(usr_agnt, stk_symbol):
    headers = {'User-Agent': usr_agnt}
    url = f'https://finance.yahoo.com/quote/{stk_symbol}'
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.text, 'html.parser')
    stocks = {
        'Stock': stk_symbol,
        'price': soup.find('fin-streamer', {'class': 'Fw(b) Fz(36px) Mb(-4px) D(ib)'}).text,
        'chng_num': soup.find('div', {'class': 'D(ib) Mend(20px)'}).find_all('span')[0].text,
        'chng_per': soup.find('div', {'class': 'D(ib) Mend(20px)'}).find_all('span')[1].text,
    }
    return stocks


for stock in monitor_stocks:
    stock_data.append(fetchStocks(user_agent, stock))
    print('Getting: ', stock)

with open('stock_data.json', 'w') as f:
    json.dump(stock_data, f)
