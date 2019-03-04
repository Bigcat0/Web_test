from testsuits.base_Discuz1 import TestDiscuz1
from testsuits.base_Discuz2 import TestDiscuz2
from testsuits.base_Discuz3 import TestDiscuz3
from testsuits.base_Discuz4 import TestDiscuz4
import unittest
import sys
# sys.path.append("D:/UI-auto Test")
import HTMLTestRunner
import os

# 设置报告文件保存路径
cur_path=os.path.dirname(os.path.realpath(__file__))
report_path=os.path.join(cur_path,"report")
if not os.path.exists(report_path):os.mkdir(report_path)
# 构建
suite=unittest.TestSuite()
suite.addTest(unittest.makeSuite(TestDiscuz1))
suite.addTest(unittest.makeSuite(TestDiscuz2))
suite.addTest(unittest.makeSuite(TestDiscuz3))
suite.addTest(unittest.makeSuite(TestDiscuz4))

if __name__=="__main__":
    html_report=report_path+ r"\result.html"
    fp=open(html_report,"wb")
    # 初始化一个HTML TestRunner实例对象，用来生成报告
    runner=HTMLTestRunner.HTMLTestRunner(stream=fp,verbosity=2,title="单元测试报告",description="用例执行情况")
    runner.run(suite)