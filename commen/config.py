import configparser
import os

pro_path=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

class Config(object):
    def __init__(self,filename="default.conf"):
        self.cf=configparser.ConfigParser()
        self.cf.read(os.path.join(pro_path,"config",filename))
    def get_runtime(self,option):
        return self.cf.get("runtime",option)
    def get_server(self,option):
        return self.cf.get("server",option)
    def get_db_test(self,option):
        return self.cf.get("db_test",option)
    def get_email(self,option):
        return self.cf.get("email",option)



if __name__=="__main__":
    # print(pro_path)
    cr=Config()
    print(cr.cf.get("runtime","log_level"))