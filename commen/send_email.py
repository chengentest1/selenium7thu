import os
import smtplib
import sys
from email.mime.text import MIMEText

from commen.config import Config, pro_path

sys.path.append('..')
def send_email(report_name):
    cf=Config()
    report_file=os.path.join(pro_path,cf.get_runtime('report_dir'),report_name)
    # report_file=r'C:\Users\cheng\PycharmProjects\api_test\report\rep.html'
    with open(report_file,'rb') as f:
        body=f.read()
    #格式化email正文
    msg=MIMEText(body,'html','utf-8')
    msg["Subject"] = cf.get_email("subject")
    msg["From"] = cf.get_email("user")
    msg["To"] = cf.get_email("receiver")
    #配置email头
    smtp = smtplib.SMTP()
    smtp.connect(cf.get_email("server"))
    smtp.login(cf.get_email("user"), cf.get_email("pwd"))
    smtp.sendmail(cf.get_email("user"), cf.get_email("receiver"), msg.as_string())

    print('邮件发送成功')
if __name__ =="__main__":
    send_email('test_report.html')



