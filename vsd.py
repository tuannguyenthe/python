import requests
import pandas as pd
from bs4 import BeautifulSoup


url = 'http://vsd.vn/p6c28/danh-sach-to-chuc-dang-ky.htm'

r = requests.get(url)
soup= BeautifulSoup(r.text, "html5lib")

discard = ['Trụ sở chính','Chi nhánh','Đã ủy quyền' ]
items = soup.find_all('tr', class_='tbColorRows')
output = []
for item in items:
    x = item.find_all('td')
    y = []
    for x_item in x:
        x_item = x_item.text.strip()
        if(x_item == 'Cổ phiếu'):
            x_item = 'STK'
        elif(x_item == 'Trái phiếu'):
            x_item = 'BND'
        elif(x_item in discard):
            x_item = ''

        if(x_item == '' or x_item.isdigit()):
            continue
        else:
            y.append(x_item)
    y.append('http://vsd.vn' + item.find('a').get('href'))
    output.append(y)


