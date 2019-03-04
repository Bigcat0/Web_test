from selenium import webdriver
import unittest
from framework.browser_engine import BrowserEngin
import time


class BaseTestCase(unittest.TestCase):
    print("开始")
    def setUp(self):
        # self.driver=webdriver.Chrome("../tools/chromedriver.exe")
        # self.driver.maximize_window()
        # self.driver.implicitly_wait(5)
        # time.sleep(5)
        browser = BrowserEngin()
        self.driver = browser.open_browser()
    def tearDown(self):
        print("完成")
        # self.driver.quit()
