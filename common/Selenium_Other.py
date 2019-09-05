# -*- coding: utf-8 -*-
"""
author:Shanchi Liang
"""
import time
import random
import datetime
from utils.logger import Logger
from selenium.webdriver.common.action_chains import ActionChains


class BasePage(object):

    def __init__(self, browser):
        self.browser = browser

    def save_img(self, *loc):

        self.browser.get_screenshot_as_file('{}/{}.png'.format(os.path.abspath("D:/test/Auto_Test/img"), loc))
        logger.info("保存截图：%s", loc)

    def send_keys(self, *loc):
        """输入元素"""
        self.browser.find_element(loc[0], loc[1]).send_keys(loc[2])
        logger.info("输入关键词：%s", loc[1])
        time.sleep(1)

    def click(self, *loc):
        logger.info("点击元素，%s, %s", loc[0], loc[1])
        self.browser.find_element(loc[0], loc[1]).click()
        time.sleep(3)

    def move_to_element(self, *loc):
        """鼠标悬停操作"""
        element = self.browser.find_element_by_xpath(loc)
        ActionChains(self.browser).move_to_element(element).perform()

    def double_click(self, *loc):
        """鼠标双击"""
        element1 = self.browser.find_element_by_xpath(loc)
        ActionChains(self.browser).double_click(element1).perform()

    def test_scroll_to_the_bottom(self):
        u"""滚动到底部"""
        self.browser.execute_script("var action=document.documentElement.scrollTop=10000")
        time.sleep(1)

    def test_look_more(self):
        u"""查看更多"""
        self.browser.find_element_by_xpath("//*[@id=\"look-more\"]/span").click()
        time.sleep(1)

    def test_scroll_to_the_top(self):
        u"""滚动到顶部"""
        self.browser.execute_script("var action=document.documentElement.scrollTop=0")
        time.sleep(1)

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

    @staticmethod
    def get_every_day(*loc):
        """设置输入检索时间"""
        date_list = []
        begin_date = str(loc[0])
        end_date = str(loc[1])
        begin_date = datetime.datetime.strptime(begin_date, "%Y-%m-%d")
        end_date = datetime.datetime.strptime(end_date, "%Y-%m-%d")
        while begin_date <= end_date:
            date_str = begin_date.strftime("%Y-%m-%d")
            date_list.append(date_str)
            begin_date += datetime.timedelta(days=1)
        i = random.randint(0, (len(date_list)-1))
        j = random.randint(0, (len(date_list) - 1))
        return date_list[i], date_list[j]

    def select_every_day(self, *loc):
        """设置选择检索时间"""
        # 获取当月天数
        date_total = len(self.browser.find_elements_by_xpath(loc))
        datelist = []
        datelists = []
        for q in range(0, date_total):
            datelist.append(self.browser.find_elements_by_xpath(loc)[q].get_attribute('text'))
        # 去掉当月的未来时间
        for w in range(0, len(datelist)):
            if int(datelist[w]) <= int(time.strftime('%d', time.localtime())):
                datelists.append(datelist[w])
        return datelist, datelists

