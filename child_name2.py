from bs4 import BeautifulSoup
import requests as req
import random

url = 'https://my-calend.ru/names/russian'
page = req.get(url)
soup = BeautifulSoup(page.text, 'lxml')

z = []

for x in soup.find_all('a', href=True):
    y = x.get_text()
    z.append(y)

print('Нажмите "1" чтобы узнать именя ваших будущих детей: ')
b = str(input())

if b == '1':
    print('Мужское имя: ' + random.choice(z[113:168])  + '\n' + 'Женское имя: ' + random.choice(z[57:112]))
else:
    print('Вы ошиблись')

    
    
    
    
