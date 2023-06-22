from bs4 import BeautifulSoup
from urllib.request import urlopen, Request
from urllib.parse import urljoin, quote
import re
import pandas as pd
import pymysql

name = []
sub_page = []
conn = pymysql.connect(host='localhost',user='root',password='onenable1@',db='restaurant_db',charset='utf8')
cur = conn.cursor()
for i in range(1,6):
    
    url_base = 'https://www.mangoplate.com'
    url_sub = "/search/" + quote("강남역") + "?keyword="+ quote("강남역") +"&page=" + str(i)
    url = url_base+url_sub

    req = Request(
        url,
        headers={'User-Agent':'Mozilla/5.0'}
    )
    html = urlopen(req)
    soup = BeautifulSoup(html,"html.parser")

    list_soup = soup.find_all('div',class_="list-restaurant-item")

    for item in list_soup:
        print(item)
        title = item.find(class_='title').get_text().split('\n')[0].split('(')[0]
        sub_page_url = url_base + item.find('a')['href']
        score = float(str(item.find('strong')).split('>')[1][:3])
        name.append([title,sub_page_url,score])

for i in range(len(name)):
    print(i)
    url = name[i][1]

    req = Request(
        url,
        headers={'User-Agent':'Mozilla/5.0'}
    )
    html = urlopen(req)
    soup = BeautifulSoup(html,"html.parser")

    list_soup = soup.find_all('table',class_="info")

    for item in list_soup:
        info = soup.find_all('tr',class_="only-desktop")
        for td_item in info:
            tmp = td_item.find('td').get_text().split('\n')[0]
            name[i].append(tmp)
        menu = soup.find_all('li',class_="Restaurant_MenuItem")
        for sub_menu in menu:
            menu_name = sub_menu.find('span', class_ = "Restaurant_Menu").get_text()
            menu_price = sub_menu.find('span', class_ = 'Restaurant_MenuPrice').get_text()
            name[i].append((menu_name,menu_price))
    if len(name[i]) >= 6 :
        sql = "insert into restaurant(`res_name`, `tel_no`,`address`,`url`,`score`)values(%s,%s,%s,%s,"+ str(name[i][2]) +")"
        val = (name[i][0],name[i][4],name[i][3],name[i][1])
        cur.execute(sql,val)
        conn.commit()
        sql = 'select res_id from restaurant where res_name ="' + name[i][0] + '"'
        cur.execute(sql)
        res_id = cur.fetchall()[0][0]
        for menu_list in name[i][5:]:
            sql = "insert into menu(`menu_name`, `price`,`res_id`,`good`)values(%s,%s,%s,0)"
            val = (menu_list[0],menu_list[1],res_id)
            cur.execute(sql,val)
            conn.commit()
    
for i in name:
    print(i)
