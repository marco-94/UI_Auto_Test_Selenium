# -*- coding: utf-8 -*-
"""
author:Shanchi Liang
"""
import time
import logging


class Logger(object):
    def __init__(self, logger_name):

        # 创建一个logger
        self.logger = logging.getLogger(logger_name)
        self.logger.setLevel(logging.INFO)

        # 设置日志存放位置,日志文件名(错误和全部日志)
        log_time = time.strftime("%Y-%m-%d_%H_%M_%S_", time.localtime(time.time()))
        all_log_path = 'D:/test/Auto_Test/logs/all_log'
        error_log_path = 'D:/test/Auto_Test/logs/error_log'
        all_log_name = all_log_path + log_time + '.log'
        error_log_name = error_log_path + log_time + '.log'

        # 创建handler
        # 创建一个handler写入所有日志
        # all_filehandle = logging.FileHandler(all_log_name)
        # all_filehandle.setLevel(logging.INFO)
        # 创建一个handler写入错误日志
        # error_filehandle = logging.FileHandler(error_log_name)
        # error_filehandle.setLevel(logging.ERROR)
        # 创建一个handler输出到控制台
        controlhandle = logging.StreamHandler()
        controlhandle.setLevel(logging.INFO)

        # 定义日志输出格式
        # 以时间-日志器名称-日志级别-日志内容的形式展示
        all_log_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        # 以时间-日志器名称-日志级别-文件名-函数行号-错误内容
        # error_log_formatter = logging.Formatter(
        #     '%(asctime)s - %(name)s - %(levelname)s - %(module)s  - %(lineno)s - %(message)s')

        # 将定义好的输出形式添加到handler
        # all_filehandle.setFormatter(all_log_formatter)
        controlhandle.setFormatter(all_log_formatter)
        # error_filehandle.setFormatter(error_log_formatter)

        # 给logger添加handler
        # self.logger.addHandler(all_filehandle)
        # self.logger.addHandler(error_filehandle)
        self.logger.addHandler(controlhandle)

    def getlog(self):
        return self.logger
