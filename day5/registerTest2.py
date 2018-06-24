import ddt
import unittest

import time
from selenium import webdriver
#2,为类增加一个装饰器，装饰器类似java中的注解
#@ddt.ddt表示这个类实现数据驱动测试
from day5.csvFileManager4 import CsvFileManager4
from day5.myTestCase import MyTestCase


@ddt.ddt
class RegisterTest2(MyTestCase):
    #3，声明一个变量
    data_table=CsvFileManager4().read("test_data.csv")
    # @classmethod
    # def setUpClass(cls):
    #     cls.driver=webdriver.Chrome()
    #     cls.driver.implicitly_wait(10)
    #     cls.driver.maximize_window()
    # @classmethod
    # def tearDownClass(cls):
    #     time.sleep(30)
    #     cls.driver.quit()
    @ddt.data(*data_table)
    def test_register(self,row):
        driver=self.driver
        driver.get("http://localhost:8001/index.php?m=user&c=public&a=reg")

        driver.find_element_by_name('username').send_keys(row[0])
        driver.find_element_by_name('password').send_keys(row[1])
        driver.find_element_by_name('userpassword2').send_keys(row[2])
        driver.find_element_by_name('mobile_phone').send_keys(row[3])
        driver.find_element_by_name('email').send_keys(row[4])
        driver.find_element_by_class_name('reg_btn').click()
        dic_pit=driver.find_element_by_css_selector('form.registerform.sign > ul > li:nth-child(1) > div > span').text
        print(dic_pit)

if __name__=='__main__':
    unittest.main()