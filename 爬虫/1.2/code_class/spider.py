from bs4 import BeautifulSoup

data = [ ]
with open('web/new_index.html','r') as web_data:
    soup=BeautifulSoup(web_data,'lxml')
    imgs=soup.select('ul > li > img')
    titles =soup.select('ul > li > div.article-info > h3 > a')
    tages = soup.select('ul > li > div.article-info > p.meta-info ')
    rates=soup.select('ul > li > div.rate > span')

    # print(imgs,titles,tages,rates,sep='\n---------------------\n')
for img,title,tage ,rate in zip(imgs,titles,tages,rates):
    info={
        'title':title.get_text(),
        'tage':list(tage.stripped_strings),
        'rate':rate.get_text(),
        'img': img.get('src'),
    }
    data.append(info)
for i in data:
    if len(i['rate']) >= 3:
        print(i['title'], i['rate'])

