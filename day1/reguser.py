import time
from selenium import webdriver
driver=webdriver.Chrome()
driver.get('http://localhost:8001/index.php?m=user&c=public&a=reg')
driver.find_element_by_name('username').send_keys('chenr12')
driver.find_element_by_name('password').send_keys('123456')
driver.find_element_by_name('userpassword2').send_keys('123456')
driver.find_element_by_name('mobile_phone').send_keys('18311219812')
driver.find_element_by_name('email').send_keys('781000@qq.com')
driver.find_element_by_class_name('reg_btn').click()
time.sleep(3)
