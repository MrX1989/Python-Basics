from requests import get
from bs4 import BeautifulSoup

def currency_rates(code):
    url = 'https://www.cbr.ru/currency_base/daily/'
    response = get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    currency_infos = soup.find_all('tr')
    dates = soup.find('div', class_='filter')
    for data in dates:
        data = list((dates.text.split()))
    for currency_info in currency_infos:
        currency_info = (currency_info.text.split())
        if code in currency_info:
            nominal_value = currency_info.pop(2)
            currency_value = round(float(currency_info.pop().replace(',','.')), 2)
            print(f'На {data[0]}: {nominal_value} {code} составляет {currency_value} руб.')
            return currency_value
    return None


letter_code = str(input('Введите буквенный код валюты (на английском языке) - ')).upper()
currency_rates(letter_code)
