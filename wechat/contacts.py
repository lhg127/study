from appium.webdriver.common.mobileby import MobileBy
from BasePage.basepage import Start_app
from wechat.addmember import AddMember
from wechat.editor_mem import SelectEditor


class Contact(Start_app):
    __add = (MobileBy.XPATH, "//*[@text='添加成员']")

    # 通讯录页，点击添加成员
    def click_add_member(self):
        # 滑动屏幕 并点击
        self.sliding().click()
        # 点击添加成员
        self.driver.find_element(*self.__add).click()
        # 切换到添加成员页
        return AddMember(self.driver)

    # 用例二，通讯录页，点击编辑
    def click_editor(self):
        __edit = (MobileBy.XPATH, "//*[@resource-id='com.tencent.wework:id/h8l']")
        # 点击编辑
        self.driver.find_element(*__edit).click()
        # 进入选择成员页
        return SelectEditor(self.driver)
