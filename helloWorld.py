#-*-coding:utf-8-*-

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time



'''
#无界面
option = webdriver.ChromeOptions()
option.add_argument("headless")
driver = webdriver.Chrome(options=option)
'''


#get 方法 打开指定网址
driver = webdriver.Chrome()
#driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get('http://www.baidu.com')

#选择网页元素
#element_keyword = driver.find_element_by_id('kw')

#输入字符
#element_keyword.send_keys('python 爬虫')
#time.sleep(10)

#找到搜索按钮
# element_search_button = driver.find_element_by_id('su')
# element_search_button.click()

#print(driver.window_handles)
#print('当前页面title', driver.title)

#退出驱动关闭所有窗口
#driver.quit()

#关闭当前窗口
driver.close()