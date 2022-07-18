import requests

# 输入用户的账号密码

# 设置登录请求的请求体数据
login_data = {
    'action': 'ajaxlogin',
    'username': 'zzzzz',
    'password': 'zhangze098098',
    'remember': 'true'
}

# 设置登录网站的请求网址
login_url = 'https://wp.forchange.cn/wp-admin/admin-ajax.php'
# 请求登录网站
login_res = requests.post(login_url, data=login_data)

# 设置要请求的书籍评论页链接
comment_url = 'https://wp.forchange.cn/wp-comments-post.php'
# 输入要评论的内容
comment = '啦啦啦'

# 设置书籍评论页链接中，请求体的表单数据
comment_data = {
    'comment': comment,
    'submit': '',
    'comment_post_ID': 11069,
    'comment_parent': 0
}

# 请求评论页
comment_res = requests.post(comment_url, data=comment_data, cookies=login_res.cookies)
print(comment_res.status_code)