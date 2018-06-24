import csv
import unittest

import time

from day5.csvFileManager4 import CsvFileManager4
from day5.myTestCase import MyTestCase
from day5.page_object.loginPage import LoginPage
from day5.page_object.memberCenterPage import MemberCenterPage
import ddt
from day5.csvFileManager4 import CsvFileManager4



@ddt.ddt
class LoginTest(MyTestCase):
    list = CsvFileManager4().read("test_data1.csv")
    #这时，这个类不需要再写setup和teardow方法了.
    @ddt.data(*list)
    def test_login2(self,row):
    # def login_info(self,username='chen123',passwrod='123456'):
        ff = LoginPage(self.driver)
        ff.open()
        ff.input_name(row[0])
        ff.input_password(row[1])
        ff.click_login_button()
        time.sleep(3)
        try:
            member_conter_page = MemberCenterPage(self.driver)
            welcomeTxt = member_conter_page.get_webcome_link_text()
        except Exception as e:
            return print(e)
        self.assertEqual(welcomeTxt, "您好 %s" % row[0])

if __name__=="__main__":
    unittest.main()
