from bs4 import BeautifulSoup
import requests
url = 'https://wp.forchange.cn/resources/page/{}/'
for page in range(1,4):
    res = requests.get(url.format(page))
    bs = BeautifulSoup(res.text,'html.parser')
    article_list = bs.find_all('article',class_ = 'post')
    for img in article_list:
        link = img.find('img')['data-src']
        img_res = requests.get(link)
        name = img.find('a',class_ = 'post-title').text
        with open('闪光读书照片/{}.jpg'.format(name),'wb') as f:
           f.write(img_res.content)

           
    
            
            
        
