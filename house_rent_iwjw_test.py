from bs4 import BeautifulSoup
import requests
from _datetime import date,datetime
import time
import pymysql
import re
from urllib.parse import quote

url = 'http://www.iwjw.com/chuzu/shanghai/?kw=%E5%87%AF%E6%AC%A3%E8%B1%AA%E5%9B%AD'
web_data = requests.get(url)
soup = BeautifulSoup(web_data.text,'lxml')

#print(soup)

house_name = soup.select('div.mod-lists.mb50.clearfix > div:nth-of-type(1) > ol > li > div > h4 > b > a > i')
house_price = soup.select('div.mod-lists.mb50.clearfix > div:nth-of-type(1) > ol > li > div > h5 > i.Hp')
house_area = soup.select('div.mod-lists.mb50.clearfix > div:nth-of-type(1) > ol > li > div > h5 > i.i2')
house_layout = soup.select('div.mod-lists.mb50.clearfix > div:nth-of-type(1) > ol > li > div > h5 > i.i1')

print(house_layout)