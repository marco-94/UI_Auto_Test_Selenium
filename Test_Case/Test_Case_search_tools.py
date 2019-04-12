# -*- coding: utf-8 -*-
"""
author:Shanchi Liang
"""
import os
import time
import unittest
from random import random
from selenium import webdriver
from dateutil.parser import parse
from BeautifulReport import BeautifulReport
from selenium.webdriver.chrome.options import Options


class Test(unittest.TestCase):
    def save_img(self, img_name):
        self.browser.get_screenshot_as_file('{}/{}.png'.format(os.path.abspath("E:\\test\\8_0\\img"), img_name))

    def setUp(self):
        # self.browser = webdriver.Chrome()
        self.starttime = parse(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
        print("开始测试时间：", self.starttime)
        self.chrome_options = Options()
        # 禁止图片加载
        prefs = {"profile.managed_default_content_settings.images": 2}
        self.chrome_options.add_experimental_option("prefs", prefs)
        # 设置chrome浏览器无界面模式
        self.chrome_options.add_argument('--headless')
        self.browser = webdriver.Chrome(chrome_options=self.chrome_options)
        self.browser.set_window_size(1920, 1080)
        self.browser.get("https://weixin.sogou.com/")
        time.sleep(3)

    def tearDown(self):
        self.browser.quit()
        self.endtime = parse(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
        print("测试结束时间：", self.endtime)
        totaltime = (self.endtime - self.starttime).total_seconds()
        print("总时长：", totaltime, "秒")

    @BeautifulReport.add_test_img('时间筛选')
    def scroll_to_the_bottom(self):
        u"""时间筛选"""
        self.browser.find_element_by_xpath("//*[@id=\"query\"]").send_keys("微信")
        self.browser.find_element_by_xpath("//*[@id=\"searchForm\"]/div/input[3]").click()
        time.sleep(2)
        self.browser.find_element_by_xpath("//*[@id=\"tool_show\"]/a").click()
        time.sleep(1)
        for i in range(0, 10):
            self.browser.find_element_by_xpath("//*[@id=\"time\"]").click()
            time.sleep(1)
            total = len(self.browser.find_elements_by_xpath("//*[@id=\"tool\"]/span[1]/div/descendant::a"))
            j = random.randint(0, total-1)
            week = random.randint(1, 6)
            day = random.randint(0, 41)
            if 0 <= j < (total-1):
                self.browser.find_elements_by_xpath("//*[@id=\"tool\"]/span[1]/div/descendant::a")[j].click()
                time.sleep(1)
            elif j == (total-1):
                self.browser.find_element_by_xpath("//*[@id=\"date_start\"]").click()
                time.sleep(1)
                # 翻到上上月
                for n in range(0, 2):
                    self.browser.find_element_by_xpath("/html/body/div[6]/div[1]/a[1]").click()
                time.sleep(1)
                self.browser.find_elements_by_xpath("/html/body/div[6]/div[2]/table/tbody/descendant::tr")[week]\
                    .find_elements_by_xpath("/html/body/div[6]/div[2]/table/tbody/descendant::td")[day].click()
                time.sleep(1)
                self.browser.find_element_by_xpath("//*[@id=\"date_end\"]").click()
                time.sleep(1)
                self.browser.find_element_by_xpath("/html/body/div[7]/div[1]/a[1]").click()
                time.sleep(1)
                self.browser.find_elements_by_xpath("/html/body/div[7]/div[2]/table/tbody/descendant::tr")[week]\
                    .find_elements_by_xpath("/html/body/div[7]/div[2]/table/tbody/descendant::td")[day].click()
                time.sleep(1)
                self.browser.find_elements_by_xpath("//*[@id=\"tool\"]/span[1]/div/descendant::a")[j].click()
            self.save_img('时间筛选')


