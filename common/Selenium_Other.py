# -*- coding: utf-8 -*-
"""
author:Shanchi Liang
"""
import time
from selenium.webdriver.common.action_chains import ActionChains


class BasePage(object):

    def __init__(self, browser):
        self.browser = browser

    def move_to_element(self, loc):
        """鼠标悬停操作"""
        element = self.browser.find_element_by_xpath(loc)
        ActionChains(self.browser).move_to_element(element).perform()

    def close_page(self):
        handles = self.browser.window_handles
        self.browser.switch_to.window(handles[1])
        time.sleep(1)
        self.browser.close()
        time.sleep(1)
        handles = self.browser.window_handles
        self.browser.switch_to.window(handles[0])
        time.sleep(1)
