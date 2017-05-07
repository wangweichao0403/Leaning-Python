from bs4 import BeautifulSoup
import requests
import time

url='https://www.tripadvisor.cn/Attractions-g60763-Activities-New_York_City_New_York.html'
urls=['https://www.tripadvisor.cn/Attractions-g60763-Activities-oa{}-New_York_City_New_York.html#ATTRACTION_LIST'.format(str(i)) for i in range(30,930,30)]
def get_attractions(url,data=None):
    time.sleep(2)
    web_data=requests.get(url)
    soup=BeautifulSoup(web_data.text,'lxml')
    titles=soup.select("div.listing_info > div.listing_title > a")
    tages=soup.select('div.p13n_reasoning_v2 ')
    if data == None:
        for title,tage in zip(titles,tages):
                info = {
                    'title': title.get_text(),
                    'tage': list(tage.stripped_strings)
                }
                print(info)


for single_url in urls:
    get_attractions(single_url)