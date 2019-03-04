import unittest
from testsuits.base_testcase import BaseTestCase
from pageobjects.Disscuz_homepage import HomePage
import time




class TestDiscuz2(BaseTestCase):
    def test_Discuz2(self):
        get="http://127.0.0.1/forum.php"
        home_page=HomePage(self.driver)
        home_page.open_url(get)
        time.sleep(3)
        home_page.search("admin","root")
        self.assertIn("论坛", self.driver.title, "进入论坛")
        home_page.moren()
        self.assertIn("默认", self.driver.title, "进入默认")
        home_page.delect()
        home_page.guanli_center()
    # def test_Discuz_fa(self):
    #     home_page.logout()
        #需要登录再打开
        home_page.guanliyuan_login("root")
        home_page.luntan()
        home_page.new_bankuai()
        home_page.guanbi()
        home_page.again_search("wangwei","weishu0124")
        home_page.shua()
        home_page.new_fa()
        home_page.fa("1111111111111111111","2222222222222222222222222")
        #home_page.fasong()
        home_page.huifu("我已经回复了啦")
        home_page.logout()

if __name__=="__main__":
    # runner=unittest.TextTestRunner(verbosity=2)
    # runner.run()
    unittest.main()
