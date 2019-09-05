# -*- coding: utf-8 -*-
"""
author:Shanchi Liang
"""
import os
import sys
import time
import logging

# 项目文件根目录
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


class Logger(object):
    def __init__(self, logger_name):

        # 创建一个logger
        self.logger = logging.getLogger(logger_name)
        self.logger.setLevel(logging.INFO)

        # 设置日志存放位置,日志文件名(错误和全部日志)
        log_time = time.strftime("%Y-%m-%d_%H_%M_%S", time.localtime(time.time()))
        all_log_path = BASE_DIR + '/logs/all_log/'
        error_log_path = BASE_DIR + '/logs/error_log/'
        all_log_name = all_log_path + log_time + '.log'
        error_log_name = error_log_path + log_time + '.log'

        # 创建handler
        if not self.logger.handlers:
            # 创建一个handler写入所有日志
            all_filehandle = logging.FileHandler(all_log_name)
            all_filehandle.setLevel(logging.INFO)
            # 创建一个handler写入错误日志
            error_filehandle = logging.FileHandler(error_log_name)
            error_filehandle.setLevel(logging.ERROR)
            # 创建一个handler输出到控制台
            controlhandle = logging.StreamHandler()
            controlhandle.setLevel(logging.INFO)

            # 定义日志输出格式
            all_log_formatter = logging\
                .Formatter('%(asctime)s - %(name)s - %(funcName)s - %(lineno)d - %(levelname)s - %(message)s')
            error_log_formatter = logging.Formatter(
                '%(asctime)s - %(name)s - %(levelname)s - %(module)s  - %(lineno)d - %(message)s')

            # 将定义好的输出形式添加到handler
            all_filehandle.setFormatter(all_log_formatter)
            controlhandle.setFormatter(all_log_formatter)
            error_filehandle.setFormatter(error_log_formatter)

            # 给logger添加handler
            self.logger.addHandler(all_filehandle)
            self.logger.addHandler(error_filehandle)
            self.logger.addHandler(controlhandle)

        # 记录日志之后移除句柄
        # self.logger.removeHandler(controlhandle)

    def getlog(self):
        return self.logger
