import time
from selenium import webdriver

driver = webdriver.Chrome('/Users/zhangze/Desktop/chromedriver')
driver.implicitly_wait(3)
driver.get('https://passport.damai.cn/login')
def login():
    driver.get('https://passport.damai.cn/login')
    time.sleep(10)
# 输入网址和开始抢购的时间,时间格式为‘14:54:04’c
def buy(html,ti):
    driver.get(html)
    tf = driver.find_elements_by_class_name('select_right_list_item')
    tf[1].click()
    click1 = driver.find_element_by_class_name('buybtn')
    while True:
        t = time.strftime("%a %b %d %H:%M:%S %Y", time.localtime())
        t = t.split(' ')
        t = t[3]
        if t == ti:
            click1.click()
            break
        else:
            time.sleep(0.01)
    click2 = driver.find_element_by_tag_name('button')
    click2.click()
    
login()
buy('https://detail.damai.cn/item.htm?id=662280576526','16:25:50')