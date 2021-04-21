#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# @date: 2021/4/21 7:59 下午
# @author：langdawang678


from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging  # 这里可用接口封装的

from appium.webdriver import Remote


# 记录日志/失败截图  + 错误信息输出 + 抛出异常
class BasePage:
    # def __init__(self, driver: WebDriver):
    def __init__(self, driver: Remote):
        '''这里改成了Remote，连接appium Server的时候就是：
        driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desire_caps)'''

        # 初始化driver
        self.driver = driver

    # =========================================================
    # =========================================================如下是appium部分的方法
    # 获取设备大小
    def get_device_size(self):
        return self.driver.get_window_size()

    # 滑屏操作
    def swipe_by_direction(self, direction):
        """"""
        size = self.get_device_size()
        if direction == "up":
            self.driver.swipe(size["width"] * 0.5, size["height"] * 0.9, size["width"] * 0.5, size["height"] * 0.5)

    # 列表滑动 - 找文本/找元素/向上/向下
    # toast获取

    # 混合应用 - 获取所有的，然后切换一下，webview的名称
    # 微信小程序