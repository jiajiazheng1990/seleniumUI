# -*-coding:utf-8-*-

from time import sleep
import unittest, random, sys
sys.path.append("./models")
sys.path.append("./page_obj")
from models import myunit, function
from page_obj.loginPage import Login


class LoginTest(myunit.MyTest):
    '''测试用户登录'''
    def user_login_verify(self, username='', password=''):
        Login(self.driver).user_login(username, password)

    def test_login1(self):
        '''用户名、密码为空登录'''
        self.user_login_verify()
        po = Login(self.driver)
        self.assertEqual(po.user_error_hint(), u"账号不能为空")
        self.assertEqual(po.pawd_error_hint(), u"密码不能为空")
        function.insert_img(self.driver, "user_pawd_empty.jpg")

    def test_login2(self):
        '''用户名正确,密码为空登录'''
        self.user_login_verify(username="*******")
        po = Login(self.driver)
        self.assertEqual(po.pawd_error_hint(), "密码不能为空")
        function.insert_img(self.driver, "paqd_empty.jpg")

    def test_login3(self):
        '''用户名为空,密码正确'''
        self.user_login_verify(password="*******")
        po = Login(self.driver)
        self.assertEqual(po.user_error_hint(), u"账号不能为空")
        function.insert_img(self.driver, "user_empty.jpg")

    def test_login4(self):
        '''用户名与密码不匹配'''
        character = random.choice('abcdefghijklmnopqrstuvwxyz')
        username = "zhangsan" + character
        self.user_login_verify(username=username, password="123456")
        po = Login(self.driver)
        self.assertEqual(po.pawd_error_hint(), u"密码与账号不匹配")
        function.insert_img(self.driver, "user_pwad_error.jpg")

    def test_login5(self):
        '''用户名、密码正确'''
        self.user_login_verify(username='********@qq.com', password='********')
        sleep(2)
        po = Login(self.driver)
        self.assertEqual(po.user_login_success(), u'Ztiny')
        function.insert_img(self.driver, "user_pwd_ture.jpg")


if __name__ == '__main__':
    unittest.main()