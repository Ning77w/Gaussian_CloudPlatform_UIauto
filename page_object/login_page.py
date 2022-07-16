#coding:utf-8
#@author: wangning
#@time: 2022/07/11 10:56
#@desc: 登录页面模型，实现登陆页面对象
from time import sleep

from common_base.selenium_base import selenium_base
from selenium.webdriver.common.by import By
from selenium import webdriver
from locator.loc_loginpage import login_locater
#from common_base.tesserate_base import Ver


class LoginPage(selenium_base):

    def login(self, username, pwd):
        self.load_page(login_locater.url)
        # if len(str(self.find_elements(login_locater.Verification))) > 0:
        #     driver.save_screenshot('All.png')
        #     img = self.find_elements(login_locater.Verification)
        #     text = Ver(img)
        self.elements_input(login_locater.username,username,"输入用户名")
        self.elements_input(login_locater.password,pwd,"输入密码")
        self.elements_click(login_locater.login_botton,"点击登录")
        self.find_elements(login_locater.title)
        results = self.get(login_locater.title,Type='title',name='',page_name='登录页')
        return results



    def login_out(self):
        pass





if __name__ == '__main__':
    driver = webdriver.Chrome()
    username = 'superadmin'
    password = '123'
    LoginPage(driver).login(username, password)
