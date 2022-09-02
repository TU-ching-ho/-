# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
url= 'https://www.ptt.cc/bbs/Food/index.html'
html = requests.get(url) 
html.encoding="utf-8" 
sp = BeautifulSoup(html.text,'html.parser')

links = sp.find_all("div", class_="title")
for link in links:
 adata = link.find("a")
 #print(adata)
 print("http://www.ptt.cc" + adata['href'], adata.text)

