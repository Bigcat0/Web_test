import unittest
from testsuits.base_testcase import BaseTestCase
from pageobjects.Disscuz_homepage import HomePage
import time
from ddt import ddt,data,unpack



@ddt
class TestDiscuz3(BaseTestCase):
    @data(["haotest"])
    @unpack
    def test_Discuz3(self,ex):
        get="http://127.0.0.1/forum.php"
        home_page=HomePage(self.driver)
        home_page.open_url(get)
        time.sleep(3)
        home_page.again_search("wangwei","weishu0124")
        time.sleep(3)
        self.assertIn("论坛", self.driver.title, "进入论坛")

        home_page.sousuoWen("haotest")
        home_page.sousuo()
        self.assertIn("搜索", self.driver.title, "开始搜索")
        #点击搜索内容
        home_page.Dresult()
        # assert "haotest" in self.driver.title


        result = home_page.yanzheng()
        self.assertEqual(result, ex, msg=result)




        home_page.logout()

if __name__=="__main__":
    unittest.main()