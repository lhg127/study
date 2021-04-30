from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy

from BasePage.basepage import Start_app
from wechat.eaditcontact import EaditContact


# 添加成员页
class AddMember(Start_app):
    __inputs = (MobileBy.XPATH, "//*[@text='手动输入添加']")
    __back = (MobileBy.XPATH, "//*[@resource-id='com.tencent.wework:id/h86']")

    def click_eadit_add(self):
        # 点击手动输入添加
        self.driver.find_element(*self.__inputs).click()
        # 切换到编辑成员页
        return EaditContact(self.driver)

    def back_addmember(self):
        # 验证保存,如果find能找到【添加成功】说明以保存成功，则不想要在进行断言
        self.driver.find_element(MobileBy.XPATH, "//*[@text='添加成功']")
        # 点击返回到通讯录页
        self.driver.find_element(*self.__back).click()
