from appium.webdriver.common.mobileby import MobileBy
from BasePage.basepage import Start_app


# 添加成员编辑页，并保存
class EaditContact(Start_app):
    __user = (MobileBy.XPATH, "//*[@resource-id='com.tencent.wework:id/b77']//*[@text='必填']")
    # __tex = "节日快乐"
    __inpu = (MobileBy.XPATH, "//*[@resource-id='com.tencent.wework:id/f4m']")
    __iphon = (MobileBy.XPATH, "//*[@resource-id='com.tencent.wework:id/f4m']")
    # __num = "13571651234"
    __save = (MobileBy.XPATH, "//*[@text='保存']")

    def eadit_contact(self, name, iphones):
        from wechat.addmember import AddMember
        # 输入用户名
        self.driver.find_element(*self.__user).send_keys(name)
        # 点击电话输入框
        self.driver.find_element(*self.__inpu).click()
        # 输入电话号码
        self.driver.find_element(*self.__iphon).send_keys(iphones)
        # 点击保存
        self.driver.find_element(*self.__save).click()
        # 回到添加成员页
        return AddMember(self.driver)
