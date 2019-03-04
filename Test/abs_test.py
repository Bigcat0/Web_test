from Test.demo1 import abs
import unittest
from ddt import ddt,data,unpack
@ddt
class ABsTest(unittest.TestCase):
    def setUp(self):
        print('开始测试............')
    @data([-1,1],[1,1],[0,0])
    @unpack
    def test_abs(self,n,ex):
        result = abs(n)
        self.assertEqual( result, ex, msg=result )
    def tearDown(self):
        print("结束测试...........")
if __name__=="__main__":
    unittest.main(verbosity=2)

