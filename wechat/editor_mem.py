from time import sleep

from appium.webdriver.common.mobileby import MobileBy
from BasePage.basepage import Start_app
from wechat.editormember import EditorMember


class SelectEditor(Start_app):
    def select_member(self):
        __sel = (MobileBy.XPATH, "//*[@text='梁坤']")
        # 选择联系人成员
        self.driver.find_element(*__sel).click()
        # 进入编辑成员页
        return EditorMember(self.driver)

    def back_contacts(self):
        __back = (MobileBy.XPATH, "//*[@resource-id='com.tencent.wework:id/h8g']")
        # 返回通讯录页
        self.driver.find_element(*__back).click()
