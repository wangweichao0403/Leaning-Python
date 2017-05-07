import requests
from bs4 import BeautifulSoup
import time

url_page=[]
url_orign=['http://bj.xiaozhu.com/search-duanzufang-p{}-0/'.format(str(i)) for i in range(2,3)]

for url_num in url_orign:
    time.sleep(2)
    web_data=requests.get(url_num)
    soup=BeautifulSoup(web_data.text,'lxml')
    urls=soup.select("#page_list > ul > li > a")
    for url in urls:
        url_page.append(url.get('href'))

def print_gender(class_name):
    if class_name == 'member_girl_ico':
        return '女'
    if class_name == 'member_boy_ico':
        return '男'

def get_attractions(url,data=None):
    time.sleep(4)
    web_data=requests.get(url)
    soup=BeautifulSoup(web_data.text,'lxml')
    title=soup.select("div.pho_info > h4 ")[0].get_text()
    address =soup.select("div.pho_info > p > span")[0].get_text()
    price=soup.select("div.day_l > span")[0].text
    img=soup.select("img[id=curBigImage]")[0].get('src')
    img_host=soup.select(" div.member_pic > a > img")[0].get('src')
    host_name=soup.select("div.w_240 > h6 > a")[0].get_text()
    gender=soup.select("div.w_240 > h6 > span")[0].get('class')[0]
    if data == None:
        info = {
            'title': title,
            'address': address,
            'price': price,
            'img': img,
            'img_host': img_host,
            'host_name': host_name,
            'gender': print_gender(gender),
        }
        print(info)
for url in url_page:
    get_attractions(url,data=None)

