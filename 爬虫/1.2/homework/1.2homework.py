from bs4 import BeautifulSoup
data=[]
with open('index.html') as web_data:
    soup=BeautifulSoup(web_data,'lxml')
    imgs=soup.select('div.thumbnail > img')
    titles = soup.select('div.caption > h4 > a')
    prices = soup.select('div.caption > h4')
    reviews = soup.select('div.ratings > p.pull-right')
    stars = soup.select('div.ratings > p:nth-of-type(2)')

for img,title,price,review,star in zip(imgs,titles,prices,reviews,stars):
    info={
        'img':img.get('src'),
        'title':title.get_text(),
        'price':price.get_text(),
        'review':review.get_text(),
        'star':len(star.find_all('span',class_='glyphicon glyphicon-star'))
        # 使用find_all 统计有几处是★的样式, 第一个参数定位标签名, 第二个参数定位css样式, 具体可以参考BeautifulSoup
        # 文档示例http: // www.crummy.com / software / BeautifulSoup / bs4 / doc
    }
    data.append(info)
print(data)
