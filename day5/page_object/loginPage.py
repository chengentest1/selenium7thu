#这种框架的设计思想，叫做page-object设计模式，是一种高级设计思想
#这种思想的主旨是把业务逻辑和代码技术分离
#测试用例的类，专门负责业务逻辑
#元素定位和操作交给 网页对象
from selenium import webdriver
from selenium.webdriver.common.by import By


class LoginPage:

    #为这个网页创建一个构造函数
    def __init__(self,driver):
        self.driver=driver
        self.url='http://localhost:8001/index.php?m=user&c=public&a=login'
    #这句话的意思是声明一个数组
    username_input_loc=(By.ID,"username")
    password_input_loc=(By.ID,"password")
    def open(self):
        self.driver.get(self.url)
    def input_name(self,username):
        #*表示给find_element传入的是把元组中的每个元素都分别传入，当作单独的参数
        self.driver.find_element(*self.username_input_loc).send_keys(username)
    def input_password(self,password):
        self.driver.find_element(*self.password_input_loc).send_keys(password)
    def click_login_button(self):
        self.driver.find_element(*self.password_input_loc).submit()

# if __name__=="__main__":
#     ff=LoginPage()
#     ff.open()
#     ff.input_name()
#     ff.input_password()
#     ff.click_login_button()
