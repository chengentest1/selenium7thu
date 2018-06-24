# 用unittest写一个后台登录的测试用例
#1.导包
import time
import unittest
from selenium import webdriver


#2.建类,并集成unittest.TestCase
from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select
class LoginTest(unittest.TestCase):
    # 3.重写setup和teardown方法
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(10)
        # 窗口最大化的代码,要求驱动版本必须和浏览器精准匹配
        cls.driver.maximize_window()
    @classmethod    #该方法只在类中执行一次
    def tearDownClass(cls):
        time.sleep(30)
        cls.driver.quit()

    def test_1_login(self):

        driver = self.driver
        driver.get("http://localhost:8001/index.php?m=admin&c=public&a=login")
        driver.find_element_by_name("username").send_keys("admin")
        # 有些常用的键也可以用转义字符代替,其中\t表示Tab键,\n表示enter键
        ActionChains(driver).send_keys("\tpassword").send_keys("\t1234").send_keys("\n").perform()
if __name__ == '__main__':
    unittest.main()
