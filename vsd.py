import requests
from bs4 import BeautifulSoup

url = 'http://vsd.vn/p6c28/danh-sach-to-chuc-dang-ky.htm'

r = requests.get(url)
