import unittest
from testsuits.base_testcase import BaseTestCase
from pageobjects.baidu_homepage import HomePage


class BaiduSearch(BaseTestCase):
    def test_baidu_search(self):
        get="https://www.baidu.com"
        home_page=HomePage(self.driver)
        home_page.open_url(get)
        home_page.search("java")




if __name__=="__main__":
    # runner=unittest.TextTestRunner(verbosity=2)
    # runner.run()
    unittest.main()