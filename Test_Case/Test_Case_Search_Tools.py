# -*- coding: utf-8 -*-
"""
author:Shanchi Liang
"""
import os
import time
import unittest
import random
from selenium import webdriver
# from dateutil.parser import parse
from BeautifulReport import BeautifulReport
# from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import ElementNotVisibleException


class Test(unittest.TestCase):
    img_path = "D:/test/Auto_Test/img"

    def save_img(self, img_name):
        self.browser \
            .get_screenshot_as_file('{}/{}.png'.format(os.path.abspath(self.img_path), img_name))

    def setUp(self):
        self.browser = webdriver.Chrome()
        # self.chrome_options = Options()
        # # 禁止图片加载
        # prefs = {"profile.managed_default_content_settings.images": 2}
        # self.chrome_options.add_experimental_option("prefs", prefs)
        # # 设置chrome浏览器无界面模式
        # self.chrome_options.add_argument('--headless')
        # self.browser = webdriver.Chrome(options=self.chrome_options)
        self.browser.set_window_size(1920, 1080)
        self.browser.get("https://weixin.sogou.com/")
        time.sleep(3)

    def tearDown(self):
        self.browser.quit()

    @BeautifulReport.add_test_img('时间筛选')
    def test_select_time_search(self):
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
            j = random.randint(0, (total-1))
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

    @BeautifulReport.add_test_img('类型筛选')
    def test_select_type_search(self):
        u"""类型筛选"""
        self.browser.find_element_by_xpath("//*[@id=\"query\"]").send_keys("微信")
        self.browser.find_element_by_xpath("//*[@id=\"searchForm\"]/div/input[3]").click()
        time.sleep(5)
        self.browser.find_element_by_xpath("//*[@id=\"tool_show\"]/a").click()
        time.sleep(1)
        for i in range(0, 10):
            j = random.randint(0, 3)
            self.browser.find_element_by_xpath("//*[@id=\"type\"]").click()
            # 不勾选任意类型
            if j == 0:
                self.browser.find_element_by_xpath("//*[@id=\"type_enter\"]").click()
            # 仅筛选图集类型
            elif j == 1:
                self.browser.find_element_by_xpath("//*[@id=\"check_pic\"]").click()
                self.browser.find_element_by_xpath("//*[@id=\"type_enter\"]").click()
            # 仅筛选含视频类型
            elif j == 2:
                self.browser.find_element_by_xpath("//*[@id=\"check_video\"]").click()
                self.browser.find_element_by_xpath("//*[@id=\"type_enter\"]").click()
            # 选中图集和含视频类型
            else:
                self.browser.find_element_by_xpath("//*[@id=\"check_pic\"]").click()
                self.browser.find_element_by_xpath("//*[@id=\"check_video\"]").click()
                self.browser.find_element_by_xpath("//*[@id=\"type_enter\"]").click()
            self.save_img('类型筛选')

    @BeautifulReport.add_test_img('公众号内检索')
    def test_public_address_search(self):
        u"""公众号内检索"""
        self.browser.find_element_by_xpath("//*[@id=\"query\"]").send_keys("微信")
        self.browser.find_element_by_xpath("//*[@id=\"searchForm\"]/div/input[3]").click()
        # 获取页面数据总条数
        total = len(self.browser.find_elements_by_xpath("//*[@id=\"main\"]/div[4]/ul/descendant::li"))
        # 获取当前页面全部的站点信息,放入public_address_list
        j = 0
        public_address_list = []
        while j < total:
            public_address_list. \
                append(self.browser.find_elements_by_xpath("//*[@id=\"main\"]/div[4]/ul/descendant::a")[2 + 5 * j].text)
            j += 1
        time.sleep(1)
        # 展开搜索工具
        self.browser.find_element_by_xpath("//*[@id=\"tool_show\"]/a").click()
        time.sleep(1)
        # 展开公众号输入框
        self.browser.find_element_by_xpath("//*[@id=\"search\"]").click()
        time.sleep(1)
        for i in range(0, 10):
            try:
                k = random.randint(0, (len(public_address_list)-1))
                # 输入public_address_list内的公众号信息
                self.browser.find_element_by_xpath("//*[@id=\"tool\"]/span[5]/div/form/span/input"). \
                    send_keys(public_address_list[k])
                time.sleep(1)
                # 点击检索按钮
                self.browser.find_element_by_xpath("//*[@id=\"search_enter\"]").click()
                time.sleep(3)
                self.save_img('公众号内检索')
                # 清除输入信息
                self.browser.find_element_by_xpath("//*[@id=\"search\"]").click()
                search_tool = self.browser.find_element_by_xpath("//*[@id=\"tool\"]/span[5]/div/form/span/input")
                search_tool.clear()
            except ElementNotVisibleException:
                print(self.browser.find_element_by_xpath("//*[@id=\"tool\"]/span[5]/div/form/p").text)
                continue


if __name__ == '__main__':
    unittest.main()
