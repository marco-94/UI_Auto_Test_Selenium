# -*- coding: utf-8 -*-
"""
author:Shanchi Liang
"""
import os
import sys
import time
import unittest
import random
import datetime
import arrow
from selenium import webdriver
# from dateutil.parser import parse
from BeautifulReport import BeautifulReport
from dateutil.relativedelta import relativedelta
# from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import ElementNotVisibleException

sys.path.append(r'D:\test\Auto_Test\common')
from Selenium_Other import BasePage
sys.path.append(r'D:\test\Auto_Test\utils')
from logger import Logger

logger = Logger("Test_Case_Search_Tools").getlog()


class Test(unittest.TestCase):
    url = "https://weixin.sogou.com/"
    img_path = "D:/test/Auto_Test/img"

    def save_img(self, img_name):
        self.browser.get_screenshot_as_file('{}/{}.png'.format(os.path.abspath(self.img_path), img_name))

    def setUp(self):
        self.browser = webdriver.Chrome()
        # self.chrome_options = Options()
        logger.info("选择的浏览器: %s" % self.browser)

        # # 禁止图片加载
        # prefs = {"profile.managed_default_content_settings.images": 2}
        # self.chrome_options.add_experimental_option("prefs", prefs)

        # # 设置chrome浏览器无界面模式
        # self.chrome_options.add_argument('--headless')
        # self.browser = webdriver.Chrome(options=self.chrome_options)

        self.browser.maximize_window()
        self.browser.get(self.url)
        logger.info("打开的URL为: %s" % self.url)
        time.sleep(3)
        logger.info("页面加载，等待3秒")

    def tearDown(self):
        self.browser.quit()
        logger.info("关闭浏览器")

    @BeautifulReport.add_test_img('时间筛选')
    def test_select_time_search(self):
        u"""时间筛选"""
        self.browser.find_element_by_xpath("//*[@id=\"query\"]").send_keys("微信")
        logger.info("搜索框输入关键词“微信”")

        self.browser.find_element_by_xpath("//*[@id=\"searchForm\"]/div/input[3]").click()
        logger.info("点击搜索按钮")
        time.sleep(2)

        self.browser.find_element_by_xpath("//*[@id=\"tool_show\"]/a").click()
        logger.info("展开搜索工具")
        time.sleep(1)

        for i in range(0, 20):
            try:
                self.browser.find_element_by_xpath("//*[@id=\"time\"]").click()
                logger.info("展开时间搜索框")
                time.sleep(1)

                total = len(self.browser.find_elements_by_xpath("//*[@id=\"tool\"]/span[1]/div/descendant::a"))
                if i ==0:
                    j = random.randint(0, (total-2))
                else:
                    j = random.randint(0, (total-1))
                logger.info("设定是选择非定义时间段还是选择自定义时间段：%s，%s为自定义，其它为非自定义", j, total-1)

                if 0 <= j < (total-1):
                    self.browser.find_elements_by_xpath("//*[@id=\"tool\"]/span[1]/div/descendant::a")[j].click()
                    logger.info("选择非自定义时间段：%s" % self.browser
                                .find_elements_by_xpath("//*[@id=\"tool\"]/span[1]/div/descendant::a")[j]
                                .get_attribute('text'))
                    time.sleep(1)
                    logger.info("自动搜索")

                elif j == (total-1):
                    k = random.randint(0, 1)
                    logger.info("设定是输入还是选择：%s，0为输入，1为选择", k)

                    if k ==0:
                        # 定义时间段： 最近一个月
                        date_list = BasePage(self.browser)\
                            .get_every_day(datetime.date.today() - relativedelta(months=1), datetime.date.today())

                        # 输入自定义开始时间
                        starttime = self.browser.find_element_by_xpath("//*[@id=\"date_start\"]")
                        starttime.clear()
                        logger.info("清空开始时间输入框")
                        starttime.send_keys(date_list[0])

                        logger.info("输入开始时间：%s", date_list[0])

                        # 输入自定义结束时间
                        endtime = self.browser.find_element_by_xpath("//*[@id=\"date_end\"]")
                        endtime.clear()
                        logger.info("清空结束时间输入框")
                        endtime.send_keys(date_list[1])

                        logger.info("输入结束时间：%s", date_list[1])

                        # 点击确认按钮
                        starttime.click()
                        endtime.click()
                        self.browser.find_elements_by_xpath("//*[@id=\"tool\"]/span[1]/div/descendant::a")[j]\
                            .click()
                        logger.info("点击确认按钮，进行搜索")

                    # 选择自定义时间
                    elif k == 1:
                        """自定义开始时间"""
                        self.browser.find_element_by_xpath("//*[@id=\"date_start\"]").click()
                        logger.info("展开开始时间月份表")

                        # 开始时间整个月份的xpath
                        start_month = "/html/body/div[6]/div[2]/table/descendant::a"

                        # 定义是否翻页(翻到上个月)，0为不翻页，1为翻页一次，2为翻页两次
                        btn_prev_month = random.randint(0, 2)

                        if btn_prev_month == 0:
                            # 不翻页
                            datelist = BasePage(self.browser).select_every_day(start_month)

                            w = random.randint(0, len(datelist[1])-1)
                            self.browser.find_elements_by_xpath(start_month)[w].click()
                            logger.info("选择开始时间：%s-%s", arrow.now().format("YYYY-MM"), datelist[1][w])

                        elif btn_prev_month == 1:
                            self.browser.find_element_by_xpath("/html/body/div[6]/div[1]/a[1]").click()
                            logger.info("翻到上个月")

                            datelist = BasePage(self.browser).select_every_day(start_month)

                            w = random.randint(0, len(datelist[0])-1)
                            self.browser.find_elements_by_xpath(start_month)[w].click()
                            logger.info("选择开始时间：%s-%s", arrow.now().shift(months=-1).format("YYYY-MM"), datelist[0][w])

                            self.browser.find_element_by_xpath("/html/body/div[6]/div[1]/a[2]").click()
                            logger.info("选择完时间之后，复位到当前月份")

                        elif btn_prev_month == 2:
                            BasePage(self.browser).double_click("/html/body/div[6]/div[1]/a[1]")
                            logger.info("翻到上上月")

                            datelist = BasePage(self.browser).select_every_day(start_month)

                            w = random.randint(0, len(datelist[0])-1)
                            self.browser.find_elements_by_xpath(start_month)[w].click()
                            logger.info("选择开始时间：%s-%s", arrow.now().shift(months=-2).format("YYYY-MM"), datelist[0][w])

                            BasePage(self.browser).double_click("/html/body/div[6]/div[1]/a[2]")
                            logger.info("选择完时间之后，复位到当前月份")

                        """自定义结束时间"""
                        self.browser.find_element_by_xpath("//*[@id=\"date_end\"]").click()
                        logger.info("展开结束时间月份表")

                        # 结束时间整个月份的xpath
                        end_month = "/html/body/div[7]/div[2]/table/descendant::a"

                        # 定义是否翻页(翻到上个月)，0为不翻页，1为翻页一次，2为翻页两次
                        btn_prev_month_end = random.randint(0, 2)

                        if btn_prev_month_end == 0:
                            # 不翻页
                            datelist = BasePage(self.browser).select_every_day(end_month)

                            w = random.randint(0, len(datelist[1])-1)
                            self.browser.find_elements_by_xpath(end_month)[w].click()
                            logger.info("选择时间：%s-%s", arrow.now().format("YYYY-MM"), datelist[1][w])

                        elif btn_prev_month_end == 1:
                            self.browser.find_element_by_xpath("/html/body/div[7]/div[1]/a[1]").click()
                            logger.info("翻到上个月")

                            datelist = BasePage(self.browser).select_every_day(end_month)

                            w = random.randint(0, len(datelist[0])-1)
                            self.browser.find_elements_by_xpath(end_month)[w].click()
                            logger.info("选择时间：%s-%s", arrow.now().shift(months=-1).format("YYYY-MM"), datelist[0][w])

                            self.browser.find_element_by_xpath("/html/body/div[7]/div[1]/a[2]").click()
                            logger.info("选择完时间之后，复位到当前月份")

                        elif btn_prev_month_end == 2:
                            # 翻到上上月
                            BasePage(self.browser).double_click("/html/body/div[7]/div[1]/a[1]")
                            logger.info("翻到上上月")

                            datelist = BasePage(self.browser).select_every_day(end_month)

                            w = random.randint(0, len(datelist[0])-1)
                            self.browser.find_elements_by_xpath(end_month)[w].click()
                            logger.info("选择时间：%s-%s", arrow.now().shift(months=-2).format("YYYY-MM"), datelist[0][w])

                            BasePage(self.browser).double_click("/html/body/div[7]/div[1]/a[2]")
                            logger.info("选择完时间之后，复位到当前月份")

                        # 点击确认按钮
                        self.browser.find_elements_by_xpath("//*[@id=\"tool\"]/span[1]/div/descendant::a")[j]\
                            .click()

            except ElementNotVisibleException:
                # 如果开始时间大于结束时间，本次循环结束，进入下次循环
                self.browser.refresh()
                logger.info("开始时间大于结束时间，刷新页面")

            self.save_img('时间筛选')
            logger.info("保存截图：时间筛选")

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
