import requests
url = "https://www.baidu.com/"
res = requests.get(url)
res.encoding = 'utf-8'
text = res.text
print(res.status_code)
print(text)