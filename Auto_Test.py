# -*- coding: utf-8 -*-
import unittest
from BeautifulReport import BeautifulReport

if __name__ == '__main__':
    suite_tests = unittest\
        .defaultTestLoader\
        .discover("E:/test/auto_test_local/Auto_Test/Test_Case", pattern="Test_Case_*.py",
                  top_level_dir=None)
    BeautifulReport(suite_tests)\
        .report(filename='测试报告-搜狗微信',
                description='搜狗微信',
                log_path='E:/test/auto_test_local/Auto_Test/Test_Result/Test_Report')
