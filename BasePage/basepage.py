from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver
from selenium.common.exceptions import NoSuchElementException
import logging

logging.basicConfig(level=logging.INFO)


class Start_app:
    # 构造init方法解决每个页面需要重复启动的问题
    # 给driver定义了一个WebDriver类型值为空，目的是在其他页面使用driver时可以联想到driver方法
    def __init__(self, driver: WebDriver = None):
        # 实列化driver
        self.driver = driver

        # 封装滑动方法

    def sliding(self, number=3):
        # 修改等待时间为1s，提高速度，因之前设置的为10s不修改就要10s内轮询
        self.driver.implicitly_wait(1)
        for cunt in range(number):
            try:
                # 用例一，找添加成员
                elem = self.driver.find_element(MobileBy.XPATH, "//*[@text='添加成员']")
                # 当找到添加成员后把时间修改回来
                self.driver.implicitly_wait(10)
                return elem
            except NoSuchElementException:
                # NoSuchElementException 需要导入后才可使用
                wd = self.driver.get_window_size()['width']
                hg = self.driver.get_window_size()['height']
                x = wd * 0.3
                hg = hg * 0.7
                hg1 = hg * 0.3
                time = 1000
                self.driver.swipe(x, hg, x, hg1, time)
                if cunt == number - 1:
                    self.driver.implicitly_wait(10)
                    # NoSuchElementException 需要导入后才可使用
                    raise NoSuchElementException(f"找了{cunt + 1}次没有找到")

    # 用例二滑动
    def delect_sliding(self, *__sli, num=3):
        # 修改等待时间为1s，提高速度，因之前设置的为10s不修改就要10s内轮询
        self.driver.implicitly_wait(1)
        for cunts in range(num):
            try:
                # 用例二，找删除成员
                dele = self.driver.find_element(*__sli)
                # 当找到添加成员后把时间修改回来
                self.driver.implicitly_wait(10)
                return dele
            except NoSuchElementException:
                # NoSuchElementException 需要导入后才可使用
                wd = self.driver.get_window_size()['width']
                hg = self.driver.get_window_size()['height']
                x = wd * 0.3
                hg = hg * 0.7
                hg1 = hg * 0.3
                time = 1000
                self.driver.swipe(x, hg, x, hg1, time)
                if cunts == num - 1:
                    self.driver.implicitly_wait(10)
                    # NoSuchElementException 需要导入后才可使用
                    raise NoSuchElementException(f"找了{cunts + 1}次没有找到")

    def log(self, by, value):
        logging.info(by)
        logging.info(value)
