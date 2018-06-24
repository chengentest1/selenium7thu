#在MyTestCase中，封装setUp和teardown方法
import unittest
from selenium import webdriver
import time
class MyTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
    # def setUp(self):
        cls.driver=webdriver.Chrome()
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()
    @classmethod
    def tearDownClass(cls):
    # def tearDown(self):
        time.sleep(3)
        cls.driver.quit()


