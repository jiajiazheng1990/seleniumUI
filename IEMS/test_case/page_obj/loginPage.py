# -*-coding:utf-8-*-

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from base import Page
from time import sleep


class Login(Page):
    '''
    用户登录界面
    '''
    url = ''
    # Action
    iems_login_user_loc = (By.LINK_TEXT, u'G-IEMS')
    # 弹出登录窗口
    def iems_login(self):
        self.find_element(*self.iems_login_user_loc).click()

    login_username_loc = (By.ID, 'userName')
    login_password_loc = (By.NAME, 'password')
    login_button_loc = (By.CLASS_NAME, 'btn')

    # 登录用户名
    def login_username(self, username):
        self.find_element(*self.login_username_loc).clear()
        self.find_element(*self.login_username_loc).send_keys(username)

    # 登录密码
    def login_password(self, password):
        self.find_element(*self.login_password_loc).clear()
        self.find_element(*self.login_password_loc).send_keys(password)

    # 登录按钮
    def login_button(self):
        self.find_element(*self.login_button_loc).click()

    # 统一登录入口
    def user_login(self, username="G-IEMS", password="admin123"):
        '''获取用户名和面登录'''
        self.open()
        self.iems_login()
        self.login_username(username)
        self.login_password(password)
        self.login_button()
        sleep(2)

    user_error_hint_loc = (By.LINK_TEXT, u"账号不能为空")
    pawd_error_hint_loc = (By.LINK_TEXT, u"密码不能为空")
    user_login_success_loc = (By.LINK_TEXT, u'Ztiny')

    # 用户名错误提示
    def user_error_hint(self):
        return self.find_element(*self.user_error_hint_loc).text

    # 密码错误提示
    def pawd_error_hint(self):
        return self.find_element(*self.pawd_error_hint_loc).text

    # 登录成功用户名
    def user_login_success(self):
        return self.find_element(*self.user_login_success_loc).text