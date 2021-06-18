from bs4 import BeautifulSoup
import requests as req
import random

url = 'https://my-calend.ru/names/russian'
page = req.get(url)
soup = BeautifulSoup(page.text, 'lxml')

list = []
z = list

for x in soup.find_all('a', href=True):
    table = x.get_text()
    td_list = x.select('td')
    list.append(table)

def reverse(lst):
    return lst[::-1]

print('Выберите имя будущего ребенка (1 - муж, 2 - жен, 3 - случайное имя): ')

b = str(input())

if b == '1':
    print(z[113:168])

elif b == '2':
    print(z[57:112])

elif b == '3':
    print(random.choice(z))

else:
    print('Вы ошиблись')

    
    
    
    
