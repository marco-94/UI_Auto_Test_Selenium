# -*- coding: utf-8 -*-
"""
author:Shanchi Liang
"""
import re
import os
import time
import random
import unittest
import urllib.request
from bs4 import BeautifulSoup
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

    @BeautifulReport.add_test_img('单个关键词指定检索')
    def word_only_search(self):
        u"""单个关键词指定检索"""
        self.browser.find_element_by_xpath("//*[@id=\"query\"]").send_keys("微信")
        self.browser.find_element_by_xpath("//*[@id=\"searchForm\"]/div/input[3]").click()
        time.sleep(2)
        self.save_img('单个关键词指定检索')
        
    @BeautifulReport.add_test_img('取top10关键词，随机检索')
    def word_random_search(self):
        u"""取top10关键词，随机检索"""
        url = self.browser.current_url
        response = urllib.request.urlopen(url)
        content = response.read()
        soup = BeautifulSoup(content, 'html.parser')
        href = "http://weixin.sogou.com/weixin"
        # 找到全部有这个url的标签
        tag = soup.find_all(href=re.compile(href))
        word_list = []
        for tags in tag:
            word_text = tags.get_text()
            word_list.append(word_text)
        print(word_list)
        for i in range(0, len(word_list)):
            word = random.choice(word_list)
            print(word)
            search_key = self.browser.find_element_by_xpath("//*[@id=\"query\"]")
            time.sleep(1)
            search_key.clear()
            time.sleep(1)
            search_key.send_keys(word)
            if i == 0:
                self.browser.find_element_by_xpath("//*[@id=\"searchForm\"]/div/input[3]").click()
                time.sleep(3)
                self.save_img('取top10关键词，随机检索')
            else:
                self.browser.find_element_by_xpath("//*[@id=\"scroll-header\"]/form/div/input[1]").click()
                time.sleep(3)
                self.save_img('取top10关键词，随机检索')

    @BeautifulReport.add_test_img('点击top榜单话题随机检索')
    def word_top_search(self):
        u"""点击top榜单话题随机检索"""
        for i in range(0, 10):
            j = random.randint(0, 10)
            # 属下子节点的全部a标签
            self.browser.find_elements_by_xpath("//*[@id=\"topwords\"]/descendant::a")[j].click()
            self.save_img('点击top榜单话题随机检索')
            # 切换页面句柄
            handles = self.browser.window_handles
            self.browser.switch_to.window(handles[1])
            time.sleep(3)
            self.browser.close()
            handles = self.browser.window_handles
            self.browser.switch_to.window(handles[0])

    @BeautifulReport.add_test_img('切换tab检索')
    def tab_select_search(self):
        u"""切换tab检索"""
        for i in range(0, 10):
            j = random.randint(0, 20)
            print(j)
            if j < 11 and j != 10:
                self.browser.find_elements_by_xpath("//*[@id=\"type_tab\"]/descendant::a")[j].click()
                self.save_img('切换tab检索')
            elif 11 < j < 20:
                # 浮现下拉选择框
                show_more = self.browser.find_element_by_xpath("//*[@id=\"more_anchor\"]")
                self.ActionChains(self.browser).move_to_element(show_more).perform()
                self.browser.find_elements_by_xpath("//*[@id=\"type_tab\"]/descendant::a")[j].click()
                self.save_img('切换tab检索')
            else:
                print("更多")
                continue

    @BeautifulReport.add_test_img('图片话题切换检索')
    def picture_select_search(self):
        u"""图片话题切换检索"""
        for i in range(0, 10):
            j = random.randint(0, 4)
            print(j)
            self.browser.find_elements_by_xpath("//*[@id=\"loginWrap\"]/div[4]/div[1]/div[1]/div/div/div")[j].click()
            time.sleep(1)
            self.browser.find_elements_by_xpath("//*[@id=\"loginWrap\"]/div[4]/div[1]/div[1]/div/descendant::a")[j].click()
            handles = self.browser.window_handles
            self.browser.switch_to.window(handles[1])
            time.sleep(1)
            self.browser.close()
            handles = self.browser.window_handles
            self.browser.switch_to.window(handles[0])
        self.save_img('图片话题切换检索')
