# -*- coding: utf-8 -*-
"""
author:Shanchi Liang
"""
import os
import time
import unittest
from selenium import webdriver
from dateutil.parser import parse
from BeautifulReport import BeautifulReport
from selenium.webdriver.chrome.options import Options


class Test(unittest.TestCase):
    def save_img(self, img_name):
        self.browser.get_screenshot_as_file('{}/{}.png'.format(os.path.abspath("E:\\test\\8_0\\img"), img_name))

    @BeautifulReport.add_test_img('登录进入首页')
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
        self.browser.get("https://cg168778.wornhole1.cn:38043/pc_login")
        time.sleep(5)
        self.browser.find_element_by_name("username").send_keys("gzsq_peizhi")
        self.browser.find_element_by_name("password").send_keys("gzsq_test")
        time.sleep(1)
        self.browser.find_element_by_id("submit").click()
        time.sleep(10)
        self.save_img('登录进入首页')
        time.sleep(1)

    def tearDown(self):
        self.browser.quit()
        self.endtime = parse(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
        print("测试结束时间：", self.endtime)
        totaltime = (self.endtime - self.starttime).total_seconds()
        print("总时长：", totaltime, "秒")

    @BeautifulReport.add_test_img('进入专题监控页面', '专题监控页面数据展示情况')
    def test_ZTJK(self):
        u"""测试用例:专题监控"""
        self.browser\
            .find_element_by_link_text("专题监控")\
            .click()
        time.sleep(15)
        handles = self.browser.window_handles
        time.sleep(1)
        self.save_img('进入专题监控页面')
        self.browser\
            .switch_to\
            .window(handles[1])
        print(
            self.browser
                .find_element_by_xpath('//h3[@class="sub-title"]')
                .get_attribute('textContent'), end=" "
             )
        self.browser\
            .find_element_by_xpath('//a[@tagid="430"]')\
            .click()
        time.sleep(10)
        print(
            self.browser
                .find_element_by_xpath('//a[@tagid="430"]')
                .get_attribute('textContent'), end=" "
             )
        self.browser\
            .find_element_by_css_selector(".dropdown.timeSelect")\
            .click()
        time.sleep(1)
        self.browser\
            .find_element_by_link_text("一月")\
            .click()
        time.sleep(3)
        print(
            self.browser
                .find_element_by_link_text("一月")
                .get_attribute('textContent'), end=" "
             )
        print(
            self.browser
                .find_element_by_xpath('//span[@class="totalCount"]')
                .get_attribute('textContent')
             )
        time.sleep(10)
        self.browser\
            .find_element_by_css_selector(".dropup.rowsSelect")\
            .click()
        time.sleep(1)
        self.browser \
            .find_element_by_link_text("10条") \
            .click()
        time.sleep(10)
        self.save_img('专题监控页面数据展示情况')

    @BeautifulReport.add_test_img('test_03')
    def test03(self):
        u"""test03"""
