# -*- coding: utf-8 -*-
import requests
import pandas as pd
from bs4 import BeautifulSoup

url = 'https://www.ettoday.net/news/news-list.htm'
r = requests.get(url)
soup = BeautifulSoup(r.text, "html5lib")

columns = ['date', 'tag', 'text','netsite']
table = []
for d in soup.find(class_="part_list_2").find_all('h3'):
    #print(d.find(class_="date").text, d.find('em').text,d.find('a').text)
    link  = d.find("a")["href"]
    for h in link:
       linksite=('https://www.ettoday.net/'+ link)
    #print(linksite)
    table.append([d.find('span').text, d.find('em').text, d.find('a').text,linksite])
df = pd.DataFrame(table, columns=columns)
#print(df) #今日新聞
df_sort=(df.sort_values(by='tag',ascending=False))
#print(df_sort) #標籤做排序
df_count=df.groupby('tag').count()
#print(df_count)  #計算各個標籤有多少篇文章
'''
for i in range(len(table)):
    s=(table[i][2]).strip()
    print(table[i][0],s)
'''

#找尋個版面新聞
looking = input("想找哪個版面的新聞? : ")
for i in range(len(table)): 
    s=(table[i][2]).strip()          
    if looking == table[i][1]:
        print(table[i][0],table[i][1],s)

