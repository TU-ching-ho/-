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
url = 'https://api.hahow.in/api/group/artificial-intelligence/courses?page=1'

r = requests.get(url,headers=headers)
    
root = r.json()
#print(root)

for data in root['data']:
    course=[]
    course.append(data['title'])
    course.append(data['owner']['name'])
    course.append(data['price'])
    #print(course)    
    ws.append(course)
wb.save('AIdata.xlsx')


