# -*- coding: utf-8 -*-
"""
author:Shanchi Liang
"""
import os
import sys
import time
import logging
from selenium import webdriver

sys.path.append(r'D:\test\Auto_Test\common')
from logger import Logger

logger = Logger("browser_driver").getlog()


class BrowserDriver(object):
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    chrome_driver_path = os.path.join(BASE_DIR, r"drivers\chromedriver.exe")

    def __init__(self, browser):
        self.browser = browser

    def open_browser(self):
        """启动浏览器"""
        logger.info("启动chrome浏览器")
        self.browser = webdriver.Chrome(self.chrome_driver_path)
        # self.chrome_options = Options(self.chrome_driver_path)

        # 禁止图片加载
        # prefs = {"profile.managed_default_content_settings.images": 2}
        # self.chrome_options.add_experimental_option("prefs", prefs)

        # 设置chrome浏览器无界面模式
        # self.chrome_options.add_argument('--headless')
        # self.browser = webdriver.Chrome(options=self.chrome_options)

        self.browser.maximize_window()
        time.sleep(3)

    def quit_browser(self):
        """关闭浏览器"""
        self.browser.quit()
        logger.info("关闭chrome浏览器")

