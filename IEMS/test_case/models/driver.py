# -*-coding:utf-8-*-

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


# 启动浏览器驱动
def browser():
    # 方案一：针对浏览器会自动更新为最新时
    driver_path = ChromeDriverManager().install()
    driver = webdriver.Chrome(executable_path=driver_path)
    # 方案二：固定浏览器版本对应版本driver
    # driver = webdriver.Chrome()
    return driver


if __name__ == '__main__':
    dr = browser()
    dr.get("http://www.baidu.com")
    dr.quit()