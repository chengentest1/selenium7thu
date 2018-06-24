
from day5.csvFileManager4 import CsvFileManager4
import time
import unittest
from selenium import webdriver
class RegisterTest(unittest.TestCase):
    #重写setup 和teardown方法
    @classmethod
    def setUpClass(cls):
        cls.driver=webdriver.Chrome()
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()
    @classmethod
    def tearDownClass(cls):
        time.sleep(30)
        cls.driver.quit()
    #编写一个测试用例
    def test_regiser(self):
        driver=self.driver
        driver.get("http://localhost:8001/")
        driver.find_element_by_link_text("注册").click()
        driver.switch_to.window(driver.window_handles[-1])
        for row in CsvFileManager4().read("test_data.csv"):
            driver.find_element_by_name('username').send_keys(row[0])
            driver.find_element_by_name('password').send_keys(row[1])
            driver.find_element_by_name('userpassword2').send_keys(row[2])
            driver.find_element_by_name('mobile_phone').send_keys(row[3])
            driver.find_element_by_name('email').send_keys(row[4])
            driver.find_element_by_class_name('reg_btn').click()

if __name__ == '__main__':
    unittest.main()

