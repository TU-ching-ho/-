# -*- coding: utf-8 -*-
import requests, os
from bs4 import BeautifulSoup
url = 'https://srm.com.tw/%e9%9b%bb%e5%bd%b1%e7%b0%a1%e4%bb%8b/%e7%86%b1%e6%98%a0%e4%b8%ad/'
r = requests.get(url)
sp = BeautifulSoup(r.text, 'html.parser')

datas = sp.find_all('article', class_='main_color inner-entry')

for post in datas:
    titles = post.find('a')['title']
    print(titles)
    times = post.find('div',class_='grid-entry-excerpt entry-content').text
    print(times)
    href = post.find('a')['href']
    print(href)
    src = post.find('img')['src']
    print(src)
    
    if not os.path.exists('moviephotos'):
        os.mkdir('moviephotos')
    with open('moviephotos/'+post.find('a')['title']+'.jpg','wb') as f:
        f.write(requests.get(post.find('img')['src']).content)