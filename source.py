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


def fetchStocks(stk_symbol):

    # google 'my user agent' and copy paste the string below
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'}
    # webpage to query
    url = f'https://finance.yahoo.com/quote/{stk_symbol}'
    # fetching the information from the website
    r = requests.get(url)
    # using BeautifulSoup to parse the HTML page
    soup = BeautifulSoup(r.text, 'html.parser')
    stocks = {
        'Stock': stk_symbol,
        'price': soup.find('fin-streamer', {'class': 'Fw(b) Fz(36px) Mb(-4px) D(ib)'}).text,
        'chng_num': soup.find('div', {'class': 'D(ib) Mend(20px)'}).find_all('span')[0].text,
        'chng_per': soup.find('div', {'class': 'D(ib) Mend(20px)'}).find_all('span')[1].text,
    }
    return stocks


for stock in monitor_stocks:
    stock_data.append(fetchStocks(stock))
    print('Getting: ', stock)

print(stock_data)
