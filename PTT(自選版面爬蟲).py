# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
def board_list(board):
    url = 'https://www.ptt.cc/bbs/{}/index.html'.format(board)
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "html5lib")
    no = 0
    for d in soup.find_all(class_="r-ent"):
        no += 1
        ti = d.find(class_="title").text.strip()
        au = d.find(class_="author").text.strip()
        da = d.find(class_="date").text.strip()
        print(no, "\t", da, "\t", au, "\t", ti)
        
board_list('stock')