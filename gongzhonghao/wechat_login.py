import time
from selenium import webdriver
import json

account_name = 'hualanhao@hotmail.com'
account_pwd = 'zh326159'


class WeChatLogin:

    @staticmethod
    def wechat_login():
        driver = webdriver.Chrome()

        # 登录订阅号后台
        driver.get('https://mp.weixin.qq.com/')

        # 加载订阅号后台的时间
        time.sleep(2)

        # 自动设置账号名称
        driver.find_element_by_name('account').clear()
        driver.find_element_by_name('account').send_keys(account_name)

        # 自动设置密码
        driver.find_element_by_name('password').clear()
        driver.find_element_by_name('password').send_keys(account_pwd)
        time.sleep(2)

        # 记住账号密码
        driver.find_element_by_class_name('frm_checkbox_label').click()
        time.sleep(2)

        driver.find_element_by_class_name('btn_login').click()
        time.sleep(20)

        cookies = driver.get_cookies()

        post = {}
        for ck in cookies:
            post[ck['name']] = ck['value']
        cookie_str = json.dumps(post)
        with open('cookie.txt', 'w+', encoding='utf-8') as f:
            f.write(cookie_str)
        driver.quit()
