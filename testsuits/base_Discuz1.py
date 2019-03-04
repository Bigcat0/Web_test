import unittest
from testsuits.base_testcase import BaseTestCase
from pageobjects.Disscuz_homepage import HomePage
import time




class TestDiscuz1(BaseTestCase):
    def test_Discuz1(self):
        get="http://127.0.0.1/forum.php"
        home_page=HomePage(self.driver)
        home_page.open_url(get)
        time.sleep(3)
        home_page.search("admin","root")
        self.assertIn("论坛",self.driver.title,"进入论坛")
        home_page.moren()
        self.assertIn("默认", self.driver.title, "进入默认")
        home_page.fa("wwwkgsndswwwww","内容我佛of上峰水ddd泥烦恼是的烦恼是你看看是")
        #self.assertIn("发帖", self.driver.title, "发表帖子")
        home_page.huifu("拉拉阿拉啦啦啦")
        # self.assertIn("回复", self.driver.title, "发表回复")
    # def test_Discuz_fa(self):
        home_page.logout()
        # self.assertIn("退出", self.driver.title)

if __name__=="__main__":
    # runner=unittest.TextTestRunner(verbosity=2)
    # runner.run()
    unittest.main()
