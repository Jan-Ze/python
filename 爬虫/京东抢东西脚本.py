import time
from selenium import webdriver

driver = webdriver.Chrome('/Users/zhangze/Desktop/chromedriver')
def login(account,password):
    driver.get('https://passport.jd.com/new/login.aspx')
    driver.find_element_by_xpath("//a[@clstag='pageclick|keycount|login_pc_201804112|10']").click()
    driver.find_element_by_id('loginname').send_keys(account)
    driver.find_element_by_id('nloginpwd').send_keys(password)
    driver.find_element_by_xpath('//a[@class="btn-img btn-entry"]').click()
    time.sleep(3)
# 输入网址和开始抢购的时间,时间格式为‘14:54:04’
def buy(html,ti):
    driver.get(html)
    click1 = driver.find_element_by_link_text('立即购买')
    while True:
        t = time.strftime("%a %b %d %H:%M:%S %Y", time.localtime())
        t = t.split(' ')
        t = t[3]
        if t == ti:
            click1.click()
            break
        else:
            time.sleep(0.01)
    handles = driver.window_handles
    driver.switch_to.window(handles[1])
    click2 = driver.find_element_by_class_name('common-submit-btn')
    click2.click()
    click3 = driver.find_element_by_id('order-submit')
    click3.click()
    
login('18818410388','zhangze098098')
buy('https://item.jd.com/100026667904.html#crumb-wrap','17:06:20')


