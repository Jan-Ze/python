import requests
from bs4 import BeautifulSoup

# 设置登录网站的请求链接
url_login = 'https://wordpress-edu-3autumn.localprod.oc.forchange.cn/wp-login.php'

# 设置博客的评论请求链接
url_comment = 'https://wordpress-edu-3autumn.localprod.oc.forchange.cn/wp-comments-post.php'

# 设置博客详情页链接
url_blog = 'https://wordpress-edu-3autumn.localprod.oc.forchange.cn/all-about-the-future_01/'

# 设置请求头
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.55 Safari/537.36'
}


# 设置登录请求的请求体数据
data_login = {
    'log': 'testzz',
    'pwd': 'zhangze098098',
    'wp-submit': '登录',
    'redirect_to': 'https://wordpress-edu-3autumn.localprod.oc.forchange.cn',
    'testcookie': '1'
}

# 请求登录网站
login = requests.post(url_login, headers=headers, data=data_login)

# 打印 Cookies 值
print(login.cookies)

# 对 Cookies 进行赋值
cookies = login.cookies

# 设置博客评论页链接中，请求体的表单数据
data_comment = {
    'comment': input('请输入你想要发表的评论：'),
    'submit': '发表评论',
    'comment_post_ID': '13',
    'comment_parent': '0'
}

# 提交评论
comment = requests.post(url_comment, headers=headers, data=data_comment, cookies=cookies)

# 若请求状态码为 200，则评论发送成功
if comment.status_code == 200:
    print('评论发送成功！')
else:
    print('评论发送失败！请求状态码为{}'.format(comment.status_code))

# 获取博客详情页信息
blog = requests.get(url_blog, headers=headers)

# 解析博客详情页信息
bs = BeautifulSoup(blog.text, 'html.parser')

# 获取包含评论信息的标签
comments = bs.find_all('div', class_='comment-content')

# 遍历标签，获取文本信息
for comment in comments:
    print(comment.find('p').text)