from bs4 import BeautifulSoup
import requests
import csv
cook_info = []
heads = ['名字','材料','链接']
url = 'https://www.xiachufang.com/explore/'
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.55 Safari/537.36'
    }
res = requests.get(url,headers = headers)
print(res.status_code)
bs = BeautifulSoup(res.text,'html.parser')
cook_list = bs.find_all('div', class_ = 'info pure-u')
new_url = 'https://www.xiachufang.com/'
for cook in cook_list:
    cook_dic = {}
    content = cook.find('a').text.replace(' ','')
    content = content.replace('\n','')
    cook_dic['名字'] = content
    cailiao = ''
    material = cook.find('p', class_ = 'ing ellipsis').find_all('a')
    for i in material:
        cailiao = cailiao + i.text + ','
    cook_dic['材料'] = cailiao
    cook_dic['链接'] = new_url + cook.find('a')['href']
    cook_info.append(cook_dic)

with open('recipe.csv','w',encoding = 'utf-8') as f:
    writer = csv.DictWriter(f,fieldnames = heads)
    writer.writeheader()
    writer.writerows(cook_info)
    
        
    
    


