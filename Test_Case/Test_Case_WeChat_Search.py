# -*- coding: utf-8 -*-
"""
author:Shanchi Liang
"""
import re
import os
import sys
import time
import random
import logging
import unittest
# import pytesseract
import urllib.request
from bs4 import BeautifulSoup
from selenium import webdriver
# from dateutil.parser import parse
from BeautifulReport import BeautifulReport
# from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import ElementNotVisibleException, WebDriverException, NoSuchElementException

sys.path.append(r'D:\test\Auto_Test\utils')
from browser_driver import BrowserDriver
from Selenium_Other import BasePage

sys.path.append(r'D:\test\Auto_Test\common')
from logger import Logger

logger = Logger("Test_Case_Search_Tools").getlog()


class Test(unittest.TestCase):
    url = "https://weixin.sogou.com/"

    def setUp(self):
        browser = BrowserDriver(self)
        self.browser = browser.open_browser()

        self.browser.get(self.url)
        logger.info("打开的URL为: %s" % self.url)
        time.sleep(3)
        logger.info("页面加载，等待3秒")

    def tearDown(self):
        BrowserDriver(self.browser).quit_browser()

    @BeautifulReport.add_test_img('单个关键词指定检索')
    def test_word_only_search(self):
        u"""单个关键词指定检索"""

        BasePage(self.browser).send_keys("xpath", "//*[@id=\"query\"]", "微信")
        BasePage(self.browser).click("xpath", "//*[@id=\"searchForm\"]/div/input[3]")
        BasePage(self.browser).save_img('单个关键词指定检索')

    @BeautifulReport.add_test_img('取top10关键词，随机检索', '访问过多')
    def test_word_random_search(self):
        logger.info("执行测试用例：取top10关键词，随机检索")
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
            word_list.append(tags.get_text())

        for i in range(0, len(word_list)):

            try:
                word = random.choice(word_list)
                search_key = self.browser.find_element_by_xpath("//*[@id=\"query\"]")
                search_key.clear()
                search_key.send_keys(word)
                logger.info("输入关键词：%s", word)

                if i == 0:
                    self.browser.find_element_by_xpath("//*[@id=\"searchForm\"]/div/input[3]").click()
                    logger.info("搜索文章：%s", word)
                    time.sleep(3)

                else:
                    self.browser.find_element_by_xpath("//*[@id=\"scroll-header\"]/form/div/input[1]").click()
                    logger.info("搜索文章：%s", word)
                    time.sleep(3)

                BasePage(self.browser).save_img('取top10关键词，随机检索')
                logger.info("保存截图：取top10关键词，随机检索")

            except NoSuchElementException:
                BasePage(self.browser).save_img('访问过多')
                logger.info("保存截图：访问过多")

    @BeautifulReport.add_test_img('点击top榜单话题随机检索')
    def test_word_top_search(self):
        logger.info("执行测试用例：点击top榜单话题随机检索")
        u"""点击top榜单话题随机检索"""

        for i in range(0, 10):
            j = random.randint(0, 10)

            self.browser.find_elements_by_xpath("//*[@id=\"topwords\"]/descendant::a")[j].click()
            logger.info("点击话题：%s", self.browser.find_elements_by_xpath("//*[@id=\"topwords\"]/descendant::a")[j]
                        .get_attribute('text'))

            BasePage(self.browser).save_img('点击top榜单话题随机检索')
            logger.info("保存截图：点击top榜单话题随机检索")

            BasePage(self.browser).close_page()
            logger.info("关闭页面")

    @BeautifulReport.add_test_img('切换tab检索', '切换更多tab检索')
    def test_tab_select_search(self):
        logger.info("执行测试用例：切换tab检索")
        u"""切换tab检索"""

        for i in range(0, 10):
            j = random.randint(0, 20)

            if j < 11 and j != 10:
                self.browser.find_elements_by_xpath("//*[@id=\"type_tab\"]/descendant::a")[j].click()
                logger.info("点击tab：%s", self.browser.find_elements_by_xpath("//*[@id=\"type_tab\"]/descendant::a")[j]
                            .get_attribute('text'))

                BasePage(self.browser).save_img('切换tab检索')
                logger.info("保存截图：切换tab检索")

            elif 11 < j < 20:
                BasePage(self.browser).move_to_element("//*[@id=\"more_anchor\"]")
                logger.info("查看更多")

                self.browser.find_elements_by_xpath("//*[@id=\"type_tab\"]/descendant::a")[j].click()
                logger.info("点击tab：%s", self.browser.find_elements_by_xpath("//*[@id=\"type_tab\"]/descendant::a")[j]
                            .get_attribute('text'))

                BasePage(self.browser).save_img('切换更多tab检索')
                logger.info("保存截图：切换更多tab检索")

    @BeautifulReport.add_test_img('滚动图片选择检索')
    def test_roll_picture_search(self):
        logger.info("执行测试用例：滚动图片选择检索")
        u"""滚动图片选择检索"""

        for i in range(0, 10):
            j = random.randint(0, 4)

            try:

                self.browser.find_elements_by_xpath("//*[@id=\"loginWrap\"]/div[4]/div[1]/div[1]/div/descendant::p")[j]\
                    .click()
                logger.info("访问文章：%s", self.browser
                            .find_elements_by_xpath("//*[@id=\"loginWrap\"]/div[4]/div[1]/div[1]/div/descendant::p")[j]
                            .get_attribute('text'))

                time.sleep(3)

                BasePage(self.browser).save_img('滚动图片选择检索')
                logger.info("保存截图：滚动图片选择检索")

                BasePage(self.browser).close_page()
                logger.info("关闭页面")

            except WebDriverException:

                self.browser.find_element_by_xpath("//*[@id=\"loginWrap\"]/div[4]/div[1]/div[1]/div/a[7]").click()
                logger.info("滚动图片")

                time.sleep(1)

    @BeautifulReport.add_test_img('图片话题切换检索')
    def test_picture_select_search(self):
        logger.info("执行测试用例：图片话题切换检索")
        u"""图片话题切换检索"""

        for i in range(0, 10):

            j = random.randint(0, 4)

            # 点击切换到指定图片页
            self.browser.find_elements_by_xpath("//*[@id=\"loginWrap\"]/div[4]/div[1]/div[1]/div/div/div")[j].click()
            time.sleep(1)

            self.browser.find_elements_by_xpath("//*[@id=\"loginWrap\"]/div[4]/div[1]/div[1]/div/descendant::a")[j]\
                .click()
            logger.info("访问文章：%s", self.browser
                        .find_elements_by_xpath("//*[@id=\"loginWrap\"]/div[4]/div[1]/div[1]/div/descendant::a")[j]
                        .get_attribute('text'))

            BasePage(self.browser).close_page()
            logger.info("关闭详情页面")

            BasePage(self.browser).save_img('图片话题切换检索')
            logger.info("保存截图：图片话题切换检索")

    @BeautifulReport.add_test_img('查看文章详情')
    def test_article_detail(self):
        logger.info("执行测试用例：查看文章详情")
        u"""查看文章详情"""

        for i in range(0, 10):

            # 获取标题总数
            total = len(self.browser.find_elements_by_xpath("//*[@id=\"pc_0_d\"]/descendant::li"))
            j = random.randint(0, total - 1)

            self.browser.find_elements_by_xpath("//*[@id=\"pc_0_d\"]/descendant::a")[1 + 4 * j].click()
            logger.info("点击标题：%s，查看文章详情", self.browser
                        .find_elements_by_xpath("//*[@id=\"pc_0_d\"]/descendant::a")[1 + 4 * j].get_attribute('text'))

            time.sleep(3)

            BasePage(self.browser).save_img('查看文章详情')
            logger.info("保存截图：查看文章详情")

            BasePage(self.browser).close_page()
            logger.info("关闭文章详情页面")

            try:
                # 查看更多
                self.browser.find_element_by_xpath("//*[@id=\"look-more\"]/span").click()
                logger.info("查看更多文章信息")

                time.sleep(1)

            except ElementNotVisibleException:
                pass

            # 滚动到底部之后，不可逆向往上查找，所以每次都要返回到顶部，再进行下一次查找
            self.browser.execute_script("var action=document.documentElement.scrollTop=0")
            logger.info("返回到页面顶部")

            time.sleep(1)


if __name__ == '__main__':
    unittest.main()
