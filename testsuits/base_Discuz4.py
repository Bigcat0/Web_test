import unittest
from testsuits.base_testcase import BaseTestCase
from pageobjects.Disscuz_homepage import HomePage
import time




class TestDiscuz4(BaseTestCase):
    def test_Discuz4(self):
        get="http://127.0.0.1/forum.php"
        home_page=HomePage(self.driver)
        home_page.open_url(get)
        time.sleep(3)
        home_page.search("wangwei","weishu0124")
        self.assertIn("论坛", self.driver.title, "进入论坛")
        home_page.moren()
        self.assertIn("默认", self.driver.title, "进入默认")
        home_page.fa_toupiao()
        ####home_page.zhuti("151515151511515")
        home_page.Writes("kkkkkkkkkkkkkkkk", "2222222222", "3333333333", "44444444444")
        home_page.Tou()
        home_page.Print()


if __name__=="__main__":

    unittest.main()