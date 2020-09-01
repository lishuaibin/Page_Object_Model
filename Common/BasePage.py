#!Users\shuai\AppData\Local\Programs python
# -*- coding:utf-8 -*-
# @Time : 2020/8/11 17:38
# @Author : shuai
# @File : BasePage.py
# @Software: PyCharm

'''
重新定需要使用的方法，并对其进行处理，方便后续使用
'''

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging
import time
import datetime
from Common import dir_config
from Common import logger
from appium.webdriver.common.mobileby import MobileBy as MB
from appium.webdriver.common.touch_action import TouchAction as TA


class BassPage:
    def __init__(self, driver):
        self.driver = driver

    # 页面截图
    def save_webImgs(self, model):
        # filePath = 截图路径 + {时间}——{模块名称}.png
        filePath = dir_config.screenshot_dir + "/{0}_{1}.png".format(
            time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime()), model)
        try:
            self.driver.save_screenshot(filePath)
            logging.info("截图成功，图片路径为:{0}".format(filePath))
        except:
            logging.exception("截图失败")

    # 封装元素等待
    # 等待元素可见-并不一定可以点击
    def wait_eleVisible(self, loc, timeout=90, poll_frequency=0.5, model=None):
        '''
        :param loc: 元素定位表达式  已定义
        :param timeout: 最大等待时间 已定义
        :param poll_frequency: 轮询频次时间 已定义
        :param model: 模块名称 未定义
        :return:
        '''
        logging.info("{1}:等待元素可见：{0}".format(loc, model))
        try:
            start = time.time()
            WebDriverWait(self.driver, timeout, poll_frequency, ).until(EC.visibility_of_element_located(loc))
            end = time.time()
            logging.info("等待时长为：{0}".format(end - start))
        except:
            logging.exception("等待元素可见失败")
            self.save_webImgs(model)
            raise

    # 等待元素可见- 可点击
    def wait_eleClickble(self, loc, timeout=30, poll_frequency=0.5, model=None):
        '''

        :param loc: 元素定位表达式
        :param timeout: 最大超时等待时间
        :param poll_frequency: 轮询频次
        :param model: 模块名称
        :return:
        '''
        logging.info("{1}:等待元素可见：{0}".format(loc, model))
        try:
            start = time.time()
            WebDriverWait(self.driver, timeout, poll_frequency, ).until(EC.element_to_be_clickable(loc))
            end = time.time()
            logging.info("等待时长为{0}".format(end - start))
        except:
            logging.exception("等待元素可见失败：{0}".format(model))
            self.save_webImgs(model)
            raise

            # 查找元素

    def get_element(self, loc, model=None):
        '''

        :param loc: 元素定位表
        :param model: 模块名称
        :return: 元素查找
        '''
        logging.info('{1}:查找元素：{0}'.format(loc, model))
        try:
            return self.driver.find_element(*loc)
        except:
            logging.exception("查找元素失败")
            # 截图
            self.save_webImgs(model)
            raise

    # 输入

    def input_text(self, loc, text, model):
        ele = self.get_element(loc)
        logging.info('{0} 在元素：{1}中输入：{2}'.format(model, loc, text))
        try:
            ele.send_keys(text)
        except:
            logging.exception("输入失败")
            self.save_webImgs(model)
            raise

    # 清除
    def clear_input_text(self, loc, model=None):
        ele = self.get_element(loc)
        try:
            logging.info("{0}:清除元素{1}的文本内容".format(model, loc))
            ele.clear()
        except:
            logging.exception("清除元素{0}的文本内容失败".format(loc))
            self.save_webImgs(model)

# 点击操作
    def click_element(self, loc, model=None):
        # 找到元素
        ele = self.get_element(loc, model)
        # 点击操作
        logging.info("{0}: 元素：{1} 点击事件。".format(model, loc))
        try:
            ele.click()
        except:
            # 捕获异常到日志中；
            logging.exception("元素：{0} 点击事件失败：".format(loc))
            # 截图 - 保存到的指定的目录。名字要想好怎么取？
            self.save_webImgs(model)
            # 抛出异常
            raise

    # 获取文本内容
    def get_text(self, loc, model=None):
        # 找到元素
        ele = self.get_element(loc, model)
        # 获取元素的文本内容
        logging.info("{0}：获取元素：{1} 的文本内容".format(model, loc))
        try:
            text = ele.text
            logging.info("{0}：元素：{1} 的文本内容为：{2}".format(model, loc, text))
            return text
        except:
            # 捕获异常到日志中；
            logging.exception("获取元素：{0} 的文本内容失败。报错信息如下：".format(loc))
            # 截图 - 保存到的指定的目录。名字要想好怎么取？
            self.save_webImgs(model)
            # 抛出异常
            raise

    # 获取元素的属性
    def get_element_attribute(self, loc, attr_name, model=None):
        # 找到元素
        ele = self.get_element(loc, model)
        # 获取元素的属性
        logging.info("{0}: 获取元素：{1} 的属性：{2}".format(model, loc, attr_name))
        try:
            value = ele.get_attribute(attr_name)
            logging.info("{0}: 元素：{1} 的属性：{2} 值为：{3}".format(model, loc, attr_name, value))
            return value
        except:
            # 捕获异常到日志中；
            logging.exception("获取元素：{0} 的属性：{1} 失败，异常信息如下：".format(loc, attr_name))
            # 截图 - 保存到的指定的目录。名字要想好怎么取？
            self.save_webImgs(model)
            # 抛出异常
            raise

    # webview切换
    def switch_webview(self, webview_name, timeout=30, poll_frequency=0.5, model=None):
        # 等待webview元素出现
        loc = (MB.CLASS_NAME, "android..webview")
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((loc)))
        # 获取所有的上下文  列表
        contexts = self.driver.contexts
        # 判断你webview 名称  是否  在当前的上下文当中，如果 在就切换，如果不在就报错。
        if webview_name in contexts:
            # 切换
            pass
        else:
            # 抛出异常。
            pass

    # 获取设备的大小

    # 获取元素的大小、坐标

    # 滑屏操作 - 向上滑屏
    def swipeUp(self, start_y_percent=0.8, end_y_percent=0.2):
        time.sleep(3)
        size = self.driver.get_window_size()
        starty = size["height"] * start_y_percent
        endy = size["height"] * end_y_percent
        x = size["width"] * 0.5
        self.driver.swipe(x, starty, x, endy, 3000)
        time.sleep(2)

    # 滑屏操作 - 向上滑屏
    def swipeDown(self, start_y_percent=0.7, end_y_percent=0.2):
        time.sleep(1)
        size = self.driver.get_window_size()
        starty = size["height"] * start_y_percent
        endy = size["height"] * end_y_percent
        x = size["width"] * 0.5
        self.driver.swipe(x, endy, x, starty, 1000)
        time.sleep(1)

    # 滑屏操作 - 向上滑屏
    def swipeLeft(self, info, start_y_percent=0.8, end_y_percent=0.2):
        # info = 获取元素尺寸大小
        size = self.driver.find_element_by_id(info)
        startx = size["width"] * start_y_percent
        endx = size["height"] * end_y_percent
        y = size["width"] * 0.5
        self.driver.swipe(startx, y, endx, y, 200)

    # toast获取
    def get_toast_msg(self, part_text, model=None):
        # xpath表达式
        xpath_loc = '//*[contains(@text,"{}")]'.format(part_text)
        logging.info("{0}: 获取toast信息，表达式为：{1}".format(model, xpath_loc))
        try:
            # 等待元素存在
            WebDriverWait(self.driver, 10, 0.01).until(EC.presence_of_element_located((MB.XPATH, xpath_loc)))
            return self.driver.find_element_by_xpath(xpath_loc).text
        except:
            # 抛异常
            logging.exception("获取toast失败")
            self.save_webImgs(model)
            raise



    # 页面坐标点击
    def click_tap(self,x,y):
        self.driver.tap(x,y)