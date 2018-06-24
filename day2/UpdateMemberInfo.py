#1,登录海盗商城
import time
from  selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

from day2.loginTest import  Login
driver=webdriver.Chrome()
Login().login(driver)

time.sleep(4)
#2，点击“账号设置”
driver.find_element_by_link_text('账号设置').click()

#3，点击“个人资料”
driver.find_element_by_link_text('个人资料').click()
#4，修改真实姓名
driver.find_element_by_id('true_name').clear()
driver.find_element_by_id('true_name').send_keys('环那')
#5，修改性别
# driver.find_element_by_id('xb').click()
# driver.execute_script("$('#xb').val('0')")
time.sleep(3)
# driver.find_elements_by_id('xb')[0].click()
# time.sleep(6)
driver.execute_script("document.getElementsByName('sex').value='0';")
time.sleep(5)
driver.find_element_by_xpath('//input[@id="xb"][@value=1]').click()
time.sleep(4)
driver.find_element_by_css_selector('[value="2"]').click()#唯一属性两边加以对中括号
#6，修改生日
driver.execute_script('$("#date").val("1900-09-09")')
# driver.execute_script('$("#date").removeAttr("readonly")')
# driver.execute_script("document.getElementById('date').removeAttribute('readonly')")
# driver.find_element_by_id('date').clear()
# driver.find_element_by_id('date').send_keys('1990-06-02')
#7，修改QQ
time.sleep(3)
driver.find_element_by_id('qq').clear()
driver.find_element_by_id('qq').send_keys('781055847')
#8，点击确定，保存成功

driver.find_element_by_class_name('btn4').click()
time.sleep(4)
driver.switch_to.alert.accept()