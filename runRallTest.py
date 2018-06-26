# 这个文件是用来批量执行unittest的测试用例
# 该文件是我们这个测试工具的唯一入口
# 1.导入unittest, 因为批量执行测试用例的功能由unittest代码库提供
import os
import smtplib
import unittest
# 注意: HTMLTestRunner的文件名和类名同名
# from package import HTMLTestRunner 这里导入的其实只是文件, 没导入类
# 所以,我们平时起名的时候, 文件名和类名最好不要完全一样, 导包的时候容易分不清
from email.mime.text import MIMEText

from commen.send_email import send_email
from package.HTMLTestRunner import HTMLTestRunner


# def send_mail(path):
#     file = open(path, 'rb')
#     msg = file.read()
#     mime = MIMEText(msg, _subtype='html', _charset="utf-8")
#     mime['Subject'] = '博为峰自动化测试报告'
#     mime['From'] = 'bwftest126@126.com'
#     to = 'changchengxc@126.com'
#     mime['To'] = to
#     smtp = smtplib.SMTP()
#     smtp.connect("smtp.126.com")
#     smtp.login('bwftest126@126.com', 'abc123asd654')
#     smtp.sendmail(from_addr='bwftest126@126.com', to_addrs=to, msg=mime.as_string())
#     smtp.quit()




if __name__ == '__main__':
    suite = unittest.defaultTestLoader.discover('./day5', pattern='*Test.py')
    base_path = os.path.dirname(__file__)
    path = base_path + '/report/test_report.html'
    # 6. 创建测试文件
    file = open(path, 'wb')
    HTMLTestRunner(stream=file, verbosity=1, title="博为峰测试报告", description="测试环境: Server 2008; 浏览器:'Chrome'").run(suite)
    send_email(path)
    # send_mail(path)