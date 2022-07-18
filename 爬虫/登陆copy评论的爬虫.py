import csv
import requests
from bs4 import BeautifulSoup

# 设置列表，用以存储每条评论的信息
head = ['用户名','评论日期','评论内容']
comment_set = []
# 设置登录网站的请求网址
login_url = 'https://wp.forchange.cn/wp-admin/admin-ajax.php'
# 输入用户的账号密码
username = 'zzzzz'
password = 'zhangze098098'

# 设置登录请求的请求体数据
ajax = {
    'action': 'ajaxlogin',
    'username': username,
    'password': password,
    'remember': 'true'
}

# 请求登录网站
login = requests.post(login_url,data = ajax)

# 设置要请求的书籍网页链接
url = 'https://wp.forchange.cn/psychology/11069/comment-page-1/'
res = requests.get(url,cookies =login.cookies )
# 携带获取到的 Cookies 信息请求书籍网页

# 解析请求到的书籍网页内容
bs = BeautifulSoup(res.text,'html.parser')

# 搜索网页中所有包含评论的 Tag
comment_list = bs.find_all('div',class_ = 'comment-txt')

for comment in comment_list:
    
# 使用 for 循环遍历搜索结果
    user = comment.find('cite',class_ = 'fn').text[:-2]
    # 提取用户名
    date = comment.find('p', class_ = 'date').text
    # 提取评论时间
    content = comment.find('div',class_ = 'bd').find('p').text
    # 提取评论内容

    dic = {
        '用户名': user,
        '评论日期': date,
        '评论内容': content
    }
    # 将评论的信息添加到字典中
    
    # 打印评论的信息
    comment_set.append(dic)
    # 存储每条评论的信息
print(len(comment_set))
with open('comment.csv','w',encoding = 'utf-8') as f:
# 新建 csv 文件，用以存储评论的信息
    writer = csv.DictWriter(f,fieldnames = head)
    # 将文件对象转换成 DictWriter 对象
    writer.writeheader()
    # 写入表头与数据
    writer.writerows(comment_set)
