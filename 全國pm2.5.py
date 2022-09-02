# -*- coding: utf-8 -*-
import requests
import json
import pandas as pd

response = requests.get("https://data.epa.gov.tw/api/v2/aqx_p_432?api_key=e8dd42e6-9b8b-43f8-991e-b3dee723a52d&limit=1000&sort=ImportDate%20desc&format=json")
dict1 = json.loads(response.text)

list1 =dict1.get("records")

county,status,pm,date,sitename=[],[],[],[],[]
for i in range(len(list1)):
    county.append(list1[i]["county"])
    status.append(list1[i]["status"])
    pm.append(list1[i]["pm2.5"])
    date.append(list1[i]["publishtime"])
    sitename.append(list1[i]["sitename"])
    
looking = input("輸入查詢區域 : ")
for i in range(len(county)):
    if looking == county[i]:       
        print("區域 : {}\tpm2.5 : {}\t空氣品質 : {}\t".format(sitename[i],pm[i],status[i]))
        

     
datas = {"縣市":county,
         "sitename":sitename,
         "pm2.5":pm,
         "空氣狀況":status,
         "更新時間":date}

pmdf = pd.DataFrame(datas)

#print(pmdf)
#pmdf.to_excel("pm2.5.xlsx",index=False)
