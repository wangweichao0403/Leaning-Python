import requests
from bs4 import BeautifulSoup
import urllib.request
import time
urls = []
def get_item_info(url):
    time.sleep(2)
    wb_data = requests.get(url)
    soup = BeautifulSoup(wb_data.text,'lxml')
    data={
        'title':soup.select('div.name_info > h1')[0].text.strip(),
         'sub_title':soup.select('h2 > span.head_title_name')[0].text.strip(),
         'author':soup.select('#author > a')[0].text,
         'publisher':soup.select('span[ddt-area="003"] > a')[0].text.strip(),
         'date': soup.select('span.t1')[2].text.split(':')[1].strip(),
         'price':soup.select('#dd-price')[0].text.strip(),
         'pinglin':soup.select('#comm_num_down')[0].text,
    }
    print(data)


def get_link(page):
    url_list=['http://category.dangdang.com/pg{}-cp01.54.12.00.00.00.html'.format(str(i+1)) for i in range(page)]
    for url in url_list:
        time.sleep(2)
        wb_data = requests.get(url)
        soup = BeautifulSoup(wb_data.text, 'lxml')
        url_li=soup.select('p.name > a')
        for link in url_li:
            urls.append(link.get('href'))
        return urls

def spider(page):
    get_link(page)
    for link in urls:
        get_item_info(link)
spider(2)


