from selenium import webdriver
driver=webdriver.Chrome()
# driver=webdriver.Chrome()
driver.implicitly_wait(20)#智能等待，查找20秒还是没有找到报错。
#如果找到了，时间不到20秒不再查找，进行下一步操作
driver.get('http://localhost:8001/')
# driver.find_element_by_link_text('登录').click()
driver.execute_script("document.getElementsByClassName('site-nav-right fr')[0].childNodes[1].removeAttribute('target')")
driver.find_element_by_css_selector('.site-nav-right.fr>a:nth-child(1)').click()

# driver.switch_to.window(driver.window_handles[1])
driver.find_element_by_name('keyword').send_keys('iphone')
driver.find_element_by_class_name('btn1').click()
