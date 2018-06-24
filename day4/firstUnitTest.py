import unittest
class FirstUnitTest(unittest.TestCase):
    def setUp(self):
        print(1)
    def tearDown(self):
        print(2)
    def test_login(self):
        print(3)
    def switch_window(self):
        print(4)
    def test_azhuce(self):
        self.switch_window()
    @classmethod
    def setUpClass(cls):
        print(5)
    @classmethod
    def tearDownClass(cls):
        print(6)
if __name__=="__main__":
    unittest.main()