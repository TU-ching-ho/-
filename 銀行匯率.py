# -*- coding: utf-8 -*-
import pandas as pd
import requests
from bs4 import BeautifulSoup
#獲取匯率的時間
url="https://rate.bot.com.tw/xrt?Lang=zh-TW"
t = requests.get(url)
sp = BeautifulSoup(t.text, "lxml")
cointime = sp.find('span',class_='time')
print(cointime.text)
    

#獲取匯率
data = pd.read_html("https://rate.bot.com.tw/xrt?Lang=zh-TW")
mydata = data[0]
print(mydata)
mydata=mydata.iloc[:,0:5]
mydata.columns=["幣別","現今匯率-本行買入","現今匯率-本行賣出","即期匯率-本行買入","即期匯率-本行賣出"]

#處理幣別重複
coin = mydata["幣別"]

s=[]
for i in range(len(coin)):
    d=(coin[i][0:10])
    s.append(d)
#print(s)
mydata = mydata.drop(columns=["幣別"])
#mydata ["幣別"]=s
mydata.insert(0,"幣別",s)
print(mydata)

