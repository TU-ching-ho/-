# -*- coding: utf-8 -*-
import tkinter as tk

def _hit1():
    import requests
    from bs4 import BeautifulSoup 
    
    url="https://www.appledaily.com.tw/realtime/hot/"
    r= requests.get(url)
    sp = BeautifulSoup(r.text,'lxml')    
    datas = sp.find_all('div',class_='flex-feature infScroll')
    for post in datas: 
        try:              
            listBox.insert(tk.END,post.find('span',class_="headline truncate truncate--3").text)
            #print(titles)
            listBox.insert(tk.END,post.find('div',class_='timestamp').string)
            #print(time)          
            link = post.find('a')['href']    
            for l in range(len(link)):
                linksite=('https://www.appledaily.com.tw/'+link)
            listBox.insert(tk.END,linksite)
            listBox.insert(tk.END,"-"*50)  
        except:
            continue
        
def _hit2():
    listBox.delete(0,tk.END)        
    
def _hit3():
    from openpyxl import Workbook
    import requests
    from bs4 import BeautifulSoup 
    
    wb = Workbook()
    ws = wb.active
    title = ['標題','時間','網址']
    ws.append(title)
    
    url="https://www.appledaily.com.tw/realtime/hot/"
    r= requests.get(url)
    sp = BeautifulSoup(r.text,'lxml')    
    datas = sp.find_all('div',class_='flex-feature infScroll')
    for post in datas:   
        course=[]
        titles = post.find('span',class_="headline truncate truncate--3").text
        #print(titles)
        course.append(titles)   
        time=post.find('div',class_='timestamp').string
        #print(time)
        course.append(time)
       
        link = post.find('a')['href']    
        for l in range(len(link)):
            linksite=('https://www.appledaily.com.tw/'+link)
        course.append(linksite)
            
        ws.append(course)  
    wb.save('news.xlsx')
    tk.messagebox.showinfo("提示","儲存完成!!!") 

wiN = tk.Tk()
sbar = tk.Scrollbar(wiN)
wiN.title("蘋果找新聞!!!")
wiN.geometry("1000x800")        

btN1 = tk.Button(wiN, text="找新聞!!",fg="red", font=("Arial", 16), width=10, height=2, command=_hit1)
btN1.pack()    

btN2 = tk.Button(wiN, text="清除!!",fg="blue", font=("Arial", 16), width=10, height=2, command=_hit2)
btN2.pack() 

btN3 = tk.Button(wiN, text="儲存!!",fg="blue", font=("Arial", 16), width=10, height=2, command=_hit3)
btN3.pack() 


sbar.pack(side=tk.RIGHT,fill=tk.Y)

listBox=tk.Listbox(wiN, font=("Arial", 20), width=100,height=100,yscrollcommand=sbar.set)
listBox.pack(side=tk.TOP,fill=tk.BOTH)    
sbar.config(command=listBox.yview)
      
wiN.mainloop()