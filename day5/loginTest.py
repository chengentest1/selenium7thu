import unittest

import time

from day5.myTestCase import MyTestCase


class LoginTest(MyTestCase):
    #这时，这个类不需要再写setup和teardow方法了.
    def test_login(self):
        driver=self.driver
        driver.get("http://localhost:8001/index.php?m=user&c=public&a=login")
        driver.find_element_by_id("username").send_keys("chen123")
        driver.find_element_by_id("password").send_keys('123456')
        old_title=driver.title
        url=driver.current_url
        driver.find_element_by_id("password").submit()

        time.sleep(3)
        text=driver.find_element_by_css_selector('div.site-nav-right.fr > a:nth-child(1)').text
        print(text)
        new_title=driver.title
        new_url=driver.current_url
        self.assertNotEqual(old_title,new_title)
        self.assertEqual(text,"您好 chen123")


if __name__=="__main__":
    unittest.main()
