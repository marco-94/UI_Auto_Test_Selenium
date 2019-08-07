# -*- coding: utf-8 -*-
"""
author:Shanchi Liang
"""
import re
import os
import time
import random
import unittest
import pytesseract
import urllib.request
from bs4 import BeautifulSoup
from selenium import webdriver
from dateutil.parser import parse
from PIL import Image, ImageEnhance
from BeautifulReport import BeautifulReport
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import ElementNotVisibleException, WebDriverException, NoSuchElementException, \
    ElementClickInterceptedException


class Test(unittest.TestCase):
    def save_img(self, img_name):
        self.browser \
            .get_screenshot_as_file('{}/{}.png'
                                    .format(os.path.abspath("D:/test/Auto_Test/img"), img_name))

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

    @BeautifulReport.add_test_img('单个关键词指定检索')
    def test_word_only_search(self):
        u"""单个关键词指定检索"""
        self.browser.find_element_by_xpath("//*[@id=\"query\"]").send_keys("微信")
        self.browser.find_element_by_xpath("//*[@id=\"searchForm\"]/div/input[3]").click()
        time.sleep(2)
        self.save_img('单个关键词指定检索')

    @BeautifulReport.add_test_img('取top10关键词，随机检索')
    def test_word_random_search(self):
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
        for i in range(0, len(word_list)):
            try:
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
                else:
                    self.browser.find_element_by_xpath("//*[@id=\"scroll-header\"]/form/div/input[1]").click()
                    time.sleep(3)
                self.save_img('取top10关键词，随机检索')
            except NoSuchElementException:
                screenImg = "E:/test/auto_test_local/Auto_Test/screenImg/screenImg.png"
                imgsrc = self.browser.find_element_by_xpath("//*[@id=\"seccodeImage\"]").get_attribute('src')
                # 浏览器页面截屏
                self.browser.get_screenshot_as_file(screenImg)
                # 定位验证码位置及大小
                location = self.browser.find_element_by_xpath("//*[@id=\"seccodeImage\"]").location
                size = self.browser.find_element_by_xpath("//*[@id=\"seccodeImage\"]").size
                left = location['x']
                top = location['y']
                right = location['x'] + size['width']
                bottom = location['y'] + size['height']
                # 从文件读取截图，截取验证码位置再次保存
                img = Image.open(screenImg).crop((left, top, right, bottom))
                img = img.convert('CMYK')  # 转换模式：L | RGB
                img = ImageEnhance.Contrast(img)  # 增强对比度
                img = img.enhance(2.0)  # 增加饱和度
                img.save(screenImg)
                # 再次读取识别验证码
                img = Image.open(screenImg)
                code = pytesseract.image_to_string(img)
                self.browser.find_element_by_xpath("//*[@id=\"seccodeInput\"]").send_keys(code.strip())
                print(code.strip())
                self.browser.find_element_by_xpath("//*[@id=\"submit\"]").click()

    @BeautifulReport.add_test_img('点击top榜单话题随机检索')
    def test_word_top_search(self):
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
    def test_tab_select_search(self):
        u"""切换tab检索"""
        for i in range(0, 10):
            j = random.randint(0, 20)
            if j < 11 and j != 10:
                self.browser.find_elements_by_xpath("//*[@id=\"type_tab\"]/descendant::a")[j].click()
                self.save_img('切换tab检索')
            elif 11 < j < 20:
                # 浮现下拉选择框
                show_more = self.browser.find_element_by_xpath("//*[@id=\"more_anchor\"]")
                ActionChains(self.browser).move_to_element(show_more).perform()
                self.browser.find_elements_by_xpath("//*[@id=\"type_tab\"]/descendant::a")[j].click()
                self.save_img('切换tab检索')
            else:
                # print("更多")
                continue

    @BeautifulReport.add_test_img('滚动图片选择检索')
    def test_roll_picture_search(self):
        u"""滚动图片选择检索"""
        for i in range(0, 10):
            j = random.randint(0, 4)
            try:
                self.browser.find_elements_by_xpath("//*[@id=\"loginWrap\"]/div[4]/div[1]/div[1]/div/descendant::p")[j] \
                    .click()
                time.sleep(3)
                self.save_img('滚动图片选择检索')
                handles = self.browser.window_handles
                self.browser.switch_to.window(handles[1])
                time.sleep(1)
                self.browser.close()
                time.sleep(1)
                handles = self.browser.window_handles
                self.browser.switch_to.window(handles[0])
                time.sleep(1)
            except WebDriverException:
                self.browser.find_element_by_xpath("//*[@id=\"loginWrap\"]/div[4]/div[1]/div[1]/div/a[7]").click()
                time.sleep(1)

    @BeautifulReport.add_test_img('图片话题切换检索')
    def test_picture_select_search(self):
        u"""图片话题切换检索"""
        for i in range(0, 10):
            j = random.randint(0, 4)
            self.browser.find_elements_by_xpath("//*[@id=\"loginWrap\"]/div[4]/div[1]/div[1]/div/div/div")[j].click()
            time.sleep(1)
            self.browser.find_elements_by_xpath("//*[@id=\"loginWrap\"]/div[4]/div[1]/div[1]/div/descendant::a")[
                j].click()
            handles = self.browser.window_handles
            self.browser.switch_to.window(handles[1])
            time.sleep(1)
            self.browser.close()
            handles = self.browser.window_handles
            self.browser.switch_to.window(handles[0])
            self.save_img('图片话题切换检索')

    @BeautifulReport.add_test_img('点击文章标题', '查看文章详情')
    def test_article_detail(self):
        u"""查看文章详情"""
        for i in range(0, 10):
            total = len(self.browser.find_elements_by_xpath("//*[@id=\"pc_0_d\"]/descendant::li"))
            j = random.randint(0, total - 1)
            # 随机点击标题，查看详情
            self.browser.find_elements_by_xpath("//*[@id=\"pc_0_d\"]/descendant::a")[1 + 4 * j].click()
            time.sleep(3)
            self.save_img('点击文章标题')
            handles = self.browser.window_handles
            self.browser.switch_to.window(handles[1])
            self.save_img('查看文章详情')
            time.sleep(1)
            self.browser.close()
            handles = self.browser.window_handles
            self.browser.switch_to.window(handles[0])
            time.sleep(1)
            try:
                # 查看更多
                self.browser.find_element_by_xpath("//*[@id=\"look-more\"]/span").click()
                time.sleep(1)
            except ElementNotVisibleException:
                pass
            # 滚动到底部之后，不可逆向往上查找，所以每次都要返回到顶部，再进行下一次查找
            self.browser.execute_script("var action=document.documentElement.scrollTop=0")
            time.sleep(1)


if __name__ == '__main__':
    unittest.main()
