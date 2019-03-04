from Test.abs_test import ABsTest
from Test.sort_test import SortTest
import unittest


# 构建
suite=unittest.TestSuite()
suite.addTest(unittest.makeSuite(ABsTest))
suite.addTest(unittest.makeSuite(SortTest))



if __name__=="__main__":
    runner=unittest.TextTestRunner(verbosity=2)
    runner.run(suite)