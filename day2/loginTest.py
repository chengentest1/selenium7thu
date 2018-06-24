from  selenium import webdriver
#1，打开浏览器
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
class Login:
    def login(self,driver):
        # driver=webdriver.Chrome()
        driver.implicitly_wait(20)
        #2，打开海盗商城网站
        driver.get('http://localhost:8001/')
        #3，删除登录链接的Terget属性
        driver.execute_script("document.getElementsByClassName('site-nav-right fr')"
                              "[0].childNodes[1].removeAttribute('target')")
        driver.find_element_by_css_selector('.site-nav-right.fr>a:nth-child(1)').click()
        driver.find_element_by_name('username').send_keys('chen123')
        # driver.find_element_by_name('password').send_keys('123456')
        ActionChains(driver).send_keys(Keys.TAB).send_keys('123456').send_keys(Keys.ENTER).perform()
        # return driver
# driver.find_element_by_id('password').send_keys('123456')
#4，点击登录按钮
# driver.find_element_by_class_name('login_btn').click()


