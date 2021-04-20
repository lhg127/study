from base_page.basepage import BasePage
from pageobject.contact_page import Contact
from time import sleep


class Homepage(BasePage):  # 首页类
    def home_page(self):  # 企业微信首页
        sleep(1)
        self.driver.find_element_by_id("menu_contacts").click()  # 切换到通讯页面
        return Contact(self.driver)  # 返回通讯页类
