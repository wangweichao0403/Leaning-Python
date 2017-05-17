from bs4 import BeautifulSoup
import requests
import time
import pymongo
import re

client=pymongo.MongoClient('localhost',27017)
tongcheng=client['tongcheng']
url_list=tongcheng['url_list']
item_info=tongcheng['item_info']

def get_links_from(channel,pages,who_sells=1):
    list_view='{}{}/pn{}/'.format(channel,str(who_sells),str(pages))
    wb_data = requests.get(list_view)
    time.sleep(1)
    soup = BeautifulSoup(wb_data.text, 'lxml')
    if soup.find('td','t'):
        links=soup.select('td.t > a.t')
        for link in links:
            item_link=link.get('href').split('?')[0]
            if re.search('jump',item_link):
                pass
            else:
                url_list.insert_one({'url':item_link})
    else:
        pass


def get_item_info(url):
    wb_data = requests.get(url)
    soup = BeautifulSoup(wb_data.text, 'lxml')
    no_longer_exist = '404' in soup.find('script', type="text/javascript").get('src').split('/')
    if no_longer_exist:
        pass
    else:
        title = soup.select('div.col_sub.mainTitle > h1')[0].text
        price = soup.select('div.su_con > span.price.c_f50')[0].text
        date = soup.select('.time')[0].text
        area = list(soup.select('.c_25d a')[0].stripped_strings) if soup.find_all('span', 'c_25d') else None
        item_info.insert_one({'title': title, 'price': price, 'date': date, 'area': area, 'url': url})
        print({'title': title, 'price': price, 'date': date, 'area': area, 'url': url})


#get_links_from('http://bj.58.com/iphonesj/',2,who_sells=1)
#get_item_info('http://bj.58.com/shouji/29791260885298x.shtml')