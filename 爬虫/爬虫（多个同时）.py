# 导入模块 requests  
import requests
from bs4 import BeautifulSoup
import csv
# 设置页码 page_number
file = 'books.csv'
#head = ['书名','作者','出版社','ISBN','页数','出版年','定价']
page_number = 1
a = []
info_real = []
# 依次取到网站书籍列表页前 3 页的网页链接，请求网页并获取响应状态码
while page_number < 10 :
    # 设置要请求的网页链接
    url = 'https://wp.forchange.cn/resources/page/' + str(page_number)
    # 请求网页
    books_list_res = requests.get(url)
    # 页码 page_number 自增
    page_number += 1
    books_list_res.encoding = 'utf-8'
    bs = BeautifulSoup(books_list_res.text,'html.parser')
    a_list = bs.find_all('a',class_='post-title')
    for url in a_list:
        info = {}
        info['书名'] = url.text
        res = requests.get(url['href'])
        res.encoding = 'utf-8'
        bs = BeautifulSoup(res.text,'html.parser')
        div = bs.find('div',class_='res-attrs')
        all_dl = div.find_all('dl')
        for dl in all_dl:
            key = dl.find('dt').text[:-2]
            value = dl.find('dd').text
            info[key] = value
        head = list(info.keys())
        info_real.append(info)

with open(file,'w',encoding = 'utf-8') as f:
    writer = csv.DictWriter(f,fieldnames = head)
    writer.writeheader()
    writer.writerows(info_real)
     
    
    
    
    
    
    

    
    
