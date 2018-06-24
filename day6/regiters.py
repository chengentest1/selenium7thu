import time
import unittest

from day5.myTestCase import MyTestCase
from day6.dbConnection import DBconnection


class Rigister(MyTestCase):
    def test_register(self):
        driver=self.driver
        driver.get("http://localhost:8001/index.php?m=user&c=public&a=reg")
        driver.find_element_by_name('username').send_keys("chen157")
        driver.find_element_by_name('password').send_keys("123456")
        driver.find_element_by_name('userpassword2').send_keys("123456")
        driver.find_element_by_name('mobile_phone').send_keys("18311183190")
        driver.find_element_by_name('email').send_keys("1773@qq.com")
        driver.find_element_by_class_name('reg_btn').click()
        time.sleep(6)
        row=DBconnection().execute_sql_command()
        self.assertEqual("chen157",row[1])
if __name__=="__main__":
    unittest.main()