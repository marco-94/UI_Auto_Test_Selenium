# -*- coding: utf-8 -*-
"""
author:Shanchi Liang
"""
import time
import random
import datetime
from selenium.webdriver.common.action_chains import ActionChains


class BasePage(object):

    def __init__(self, browser):
        self.browser = browser

    def move_to_element(self, loc):
        """鼠标悬停操作"""
        element = self.browser.find_element_by_xpath(loc)
        ActionChains(self.browser).move_to_element(element).perform()

    def close_page(self):
        """关闭新打开的页面"""
        handles = self.browser.window_handles
        self.browser.switch_to.window(handles[1])
        time.sleep(1)
        self.browser.close()
        time.sleep(1)
        handles = self.browser.window_handles
        self.browser.switch_to.window(handles[0])
        time.sleep(1)

    def get_Every_Day(self, begin_date, end_date):
        """设置检索时间"""
        date_list = []
        begin_date = str(begin_date)
        end_date = str(end_date)
        begin_date = datetime.datetime.strptime(begin_date, "%Y-%m-%d")
        end_date = datetime.datetime.strptime(end_date, "%Y-%m-%d")
        while begin_date <= end_date:
            date_str = begin_date.strftime("%Y-%m-%d")
            date_list.append(date_str)
            begin_date += datetime.timedelta(days=1)
        i = random.randint(0, (len(date_list)-1))
        j = random.randint(0, (len(date_list) - 1))
        return date_list[i], date_list[j]

