from appium.webdriver.common.mobileby import MobileBy
from BasePage.basepage import Start_app


# 编辑成员页
class EditorMember(Start_app):
    def delete_member(self):
        from wechat.editor_mem import SelectEditor
        __dele = (MobileBy.XPATH, "//*[@resource-id='com.tencent.wework:id/bei']")
        __sli = (MobileBy.XPATH, "//*[@text='删除成员']")
        # 滑动，并删除成员
        self.delect_sliding(*__sli).click()
        # 点击删除确定
        self.driver.find_element(*__dele).click()
        # 返回编辑成员页
        return SelectEditor(self.driver)
