# -*- coding: utf-8 -*-
import unittest
from BeautifulReport import BeautifulReport

if __name__ == '__main__':
    suite_tests = unittest\
        .defaultTestLoader\
        .discover("E:/test/8_0/case", pattern="test*.py", top_level_dir=None)
    BeautifulReport(suite_tests)\
        .report(filename='测试报告-专题监控', description='专题监控', log_path='E:/test/8_0/result')
