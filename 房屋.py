# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup 
from openpyxl import Workbook

wb = Workbook()
ws = wb.active
title = ['house','site','price']
ws.append(title)

header ={'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'}
url = 'https://community.houseprice.tw/list/%E5%8F%B0%E5%8D%97%E5%B8%82_city/%E4%BB%81%E5%BE%B7%E5%8D%80_zip/pop-desc_sort/?p=1'


for index in range(12):
    url = 'https://community.houseprice.tw/list/%E5%8F%B0%E5%8D%97%E5%B8%82_city/%E4%BB%81%E5%BE%B7%E5%8D%80_zip/pop-desc_sort/?p='
    url =url+str(index)
    r = requests.get(url,headers=header)

    sp = BeautifulSoup(r.text, 'html.parser')

    for mysp in sp.find_all('li'):
        try:
            c = []
            title = mysp.find('h3',class_='title_list')
            titles=title.text
            print(title.text)
            c.append(titles)
            site = mysp.find('p',class_='space_style')
            sites =(site.text).strip()
            print((site.text).strip())
            c.append(sites)
            price = mysp.find('span',class_='txt_color_p')
            money=(price.text)
            c.append(money)
            for i in range(len(price)):
                prices=money+"萬"
            print("平均單價 : ",prices)
            
            ws.append(c)
        except:
            continue
    wb.save('housedata.xlsx')