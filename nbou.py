import requests
from bs4 import BeautifulSoup


url = "https://www.oschadbank.ua/"


response = requests.get(url)

if response.status_code == 200:
    print('connect successful')
    soup = BeautifulSoup(response.text, 'html.parser')
    currency_block = soup.find('span', class_='currency__item_value')
    if currency_block:
        currency_text = currency_block.get_text(strip=True)
        if currency_text.startswith("4"):
            print(currency_text)

else:
    print('connect fail')
