import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select

driver=webdriver.Chrome()
driver.get('http://localhost:8001/index.php?m=user&c=public&a=login')
driver.find_element_by_id('username').send_keys('chen123')
driver.find_element_by_id('password').send_keys('123456')
driver.find_element_by_class_name('login_btn').click()
time.sleep(5)
p=driver.find_element_by_css_selector('.site-nav-right.fr > a:nth-child(1)').text
try:
    assert p=="您好 chen123"
except Exception as e:
    print('测试失败')
driver.find_element_by_css_selector('.kong > p > a').click()
driver.find_element_by_name('keyword').send_keys('iphone')
driver.find_element_by_class_name('btn1').click()
time.sleep(2)
driver.find_element_by_css_selector('body > div.shopCon.w1100 > div.ShopboxR.fl > div.protect_con > div > div.shop_01-imgbox > a').click()
handles=driver.window_handles
currant_windos=driver.current_window_handle
for i in handles:
    if i==currant_windos:
        pass
    else:
        driver.switch_to.window(i)
time.sleep(3)
driver.find_element_by_name('cart_num').send_keys(Keys.BACKSPACE)
driver.find_element_by_name('cart_num').send_keys('10')
time.sleep(30)
driver.find_element_by_id('joinCarButton').click()
time.sleep(2)
# driver.execute_script('onclick')
driver.find_element_by_class_name('shopCar_T_span3').click()
driver.find_element_by_css_selector('.shopCar_btn_03.fl').click()
# print(p)
driver.find_element_by_class_name('add-address').click()
driver.find_element_by_name('address[address_name]').send_keys('chen123')
driver.find_element_by_name('address[mobile]').send_keys('18311129878')
Select(driver.find_element_by_id('add-new-area-select')).select_by_value('120000')
Select(driver.find_elements_by_class_name('add-new-area-select')[1]).select_by_value('120100')
Select(driver.find_elements_by_class_name('add-new-area-select')[2]).select_by_value('120102')
driver.find_element_by_name('address[address]').send_keys('天津市河东区东大街8号院')
driver.find_element_by_name('address[zipcode]').send_keys('0128329')
driver.find_element_by_class_name('aui_state_highlight').click()




time.sleep(10)
driver.quit()