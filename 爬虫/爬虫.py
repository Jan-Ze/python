import requests
from bs4 import BeautifulSoup

# 获取网页
# 《乌合之众》网页的 URL
url = 'https://wp.forchange.cn/psychology/11069/'
# 请求网页
res = requests.get(url)
# 打印响应的状态码
print(res.status_code)
# 将响应内容的编码格式设置为utf-8
res.encoding = 'utf-8'
             
# 解析网页
# 解析请求到的网页，得到 BeautifulSoup 对象
bs = BeautifulSoup(res.text, 'html.parser')

# 搜索书籍信息的父节点<div>
info_tag = bs.find('div', class_='res-attrs')
# 搜索每条信息的节点<dl>
info_list = info_tag.find_all('dl')

# 创建字典，存储书籍信息
info_dict = {}

# 遍历搜索结果，提取文本内容，存储到字典中
for info in info_list:
    print(info.find('dt').text[:-1])
    # 提取信息提示项<dt>的元素内容
    key = info.find('dt').text[:-2]
    # 提取书籍信息<dd>的元素内容
    value = info.find('dd').text
    # 将信息添加到字典中
    info_dict[key] = value

# 打印查看字典中的书籍信息
print(info_dict)