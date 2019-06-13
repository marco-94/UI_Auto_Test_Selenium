# -*- coding: utf-8 -*-
import unittest
from BeautifulReport import BeautifulReport

if __name__ == '__main__':
    test_suite = unittest\
        .defaultTestLoader.discover("E:/test/Auto_Test/Test_Case", pattern="Test_Case_WeChat*.py")
    result = BeautifulReport(test_suite)
    result\
        .report(filename='测试报告-搜狗微信',
                description='搜狗微信',
                log_path='E:/test/Auto_Test/Test_Result/Test_Report')
