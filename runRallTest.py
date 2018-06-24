import os
import unittest

from package.HTMLTestRunner import HTMLTestRunner

if __name__=="__main__":
    suit=unittest.defaultTestLoader.discover('./day5',pattern="*test.py")
    base_path=os.path.dirname(__file__)
    path=base_path+'/report/test_report.html'
    file=open(path,'wb')
    HTMLTestRunner(stream=file, verbosity=1, title="博为峰", description="win10").run(suit)

