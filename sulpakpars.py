from bs4 import BeautifulSoup
import requests
import csv
from pprint import pprint as pp


CSV = 'sulpak_phone.csv'
HOST = 'https://www.sulpak.kg/'
URL = 'https://www.sulpak.kg/f/smartfoniy'
HEADERS = {'User-Agent' : 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:94.0) Gecko/20100101 Firefox/94.0'}

def get_html(url, params=''):
    response = requests.get(URL, headers=HEADERS, params=params, verify=False)
    return response

def get_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.findAll('div', class_ = 'goods-tiles')
    phones = []

    for item in items:
        phones.append({
            'link': HOST + item.find('div', class_='goods-photo').find('a').get('href'),
            'pr': item.find('div', class_='price').get_text(strip=True),
            't': item.find('div', class_='product-container-right-side').find('a').get_text(strip=True),
            'avai': item.find('span', class_='availability').get_text(strip=True)

        })

    return phones

def save(items, path):
    with open(path, 'a') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow(['Ссылка', 'Цена', 'Наименование', 'Наличие'])
        for item in items:
            writer.writerow([item['link'], item['pr'], item['t'], item['avai']])

def parser():
    PAGENATOR = input("Введите номер страницы: ")
    PAGENATOR = int(PAGENATOR.strip())
    html = get_html(URL)
    if html.status_code == 200:
        new_list = []
        for page in range(1, PAGENATOR):
            print(f"Страница №{page} готова")
            html = get_html(URL, params={'page':page})
            new_list.extend(get_content(html.text))
        save(new_list, CSV)
        print("Парсинг готов")
    else:
        print('error')

parser()