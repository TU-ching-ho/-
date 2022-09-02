# -*- coding: utf-8 -*-
import requests as rq
import json

url="https://od.cdc.gov.tw/eic/Day_Confirmation_Age_County_Gender_19CoV.json"

re = rq.get(url)
datas = json.loads(re.text)
