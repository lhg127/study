from appium.webdriver.common.mobileby import MobileBy
from BasePage.basepage import Start_app
from wechat.contacts import Contact


class HomePage(Start_app):
    __con = (MobileBy.XPATH, '//*[@resource-id="com.tencent.wework:id/dy5" and @text="通讯录"]')

    # 企业微信首页切换到通讯录页
    def goto_contact(self):
        # 点击通讯录
        self.driver.find_element(*self.__con).click()
        # 切换到通讯录页
        return Contact(self.driver)

    # 用例二，企业微信首页切换到通讯录页
    def goto_contacts(self):
        __con = (MobileBy.XPATH, "//*[@resource-id='com.tencent.wework:id/dy5' and @text='通讯录']")
        # 点击通讯录页
        self.driver.find_element(*__con).click()
        # 切换到通讯录页
        return Contact(self.driver)
