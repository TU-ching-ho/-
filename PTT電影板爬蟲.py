# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup 
from openpyxl import Workbook

wb = Workbook()
ws = wb.active
title = ['標題','作者','時間']
ws.append(title)

urL="https://www.ptt.cc/bbs/movie/index.html"
rQ=requests.get(urL).text
souP=BeautifulSoup(rQ,"html.parser")

for mySoup in souP.find_all("div",class_='r-ent'):
  for data in mySoup.find_all("div",class_='title'):
      try:      
          course=[]
          title=(data.find('a').text)
          print("標題: ",title)
          course.append(title)
          time = mySoup.find('div',class_="date").text
          print("時間: ",time)
          course.append(time)
          author = mySoup.find('div',class_="author").text
          print("作者: ",author)
          course.append(author)
          ws.append(course)
          print("========================================================")
      except:
          continue
wb.save('movies.xlsx')             
 
