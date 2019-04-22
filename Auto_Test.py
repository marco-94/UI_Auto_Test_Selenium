# -*- coding: utf-8 -*-
import unittest
from BeautifulReport import BeautifulReport

if __name__ == '__main__':
    suite_tests = unittest\
        .defaultTestLoader\
        .discover("E:/test/team/Auto_Test/Test_Case", pattern="Test_Case_Search_*.py",
                  top_level_dir=None)
    BeautifulReport(suite_tests)\
        .report(filename='测试报告-搜狗微信',
                description='搜狗微信',
                log_path='E:/test/team/Auto_Test/Test_Result/Test_Report')
