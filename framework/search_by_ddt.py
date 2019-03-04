from selenium import webdriver
import unittest
from ddt import data, ddt, unpack
import time
from framework.Read_excell import Util

testdata = Util.read_excel("D:/xlrd.xlsx", "Sheet1")

@ddt
class Search_by_ddt(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome("../tools/chromedriver.exe")
        self.driver.maximize_window()
        self.driver.get("https://www.baidu.com")
        self.driver.implicitly_wait(5)
    @data(*testdata)
    def test_search_by_ddt(self, data):
        search_string = data["anniumans"]
        print("搜索内容->：%s" %search_string)
        search_input = self.driver.find_element_by_id('kw')
        search_input.send_keys(search_string)
        time.sleep(3)
        search_input.submit()

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()