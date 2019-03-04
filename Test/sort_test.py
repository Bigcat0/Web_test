from Test.sort import sort
import unittest
from ddt import ddt,data,unpack
@ddt
class SortTest(unittest.TestCase):
    def setUp(self):
        print('开始测试............')
    @data([0,0,0],[1,0,2],[1,1,10],[1,2,20])
    @unpack
    def test_sort(self,n,ty,ex):
        result = sort(n,ty)
        self.assertEqual(result,ex,msg=result)
    def tearDown(self):
        print("结束测试...........")
if __name__=="__main__":
    unittest.main(verbosity=2)

