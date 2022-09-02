# -*- coding: utf-8 -*-
import requests

from openpyxl import Workbook

wb = Workbook()
ws = wb.active

title = ['課程','作者','價格']
ws.append(title)

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
    }
url = 'https://api.hahow.in/api/courses?limit=24&page=0'


for index in range(35):
    url = 'https://api.hahow.in/api/courses?limit=24&page='
    url =url+str(index)
    r = requests.get(url,headers=headers)
    
    root = r.json()
    print(root)
    for data in root['data']:
        course=[]
        course.append(data['title'])
        course.append(data['owner']['name'])
        course.append(data['price'])        
        ws.append(course)
    print(course)
wb.save('data.xlsx')


