from base_page.basepage import BasePage
from pageobject.add_department import AddDepartment


class Contact(BasePage):  # 通讯类

    def click_add_department(self):  # 添加部门
        self.driver.find_element_by_css_selector(".js_create_dropdown").click()  # 点击+号
        self.driver.find_element_by_class_name("js_create_party").click()  # 点击添加部门

        return AddDepartment(self.driver)  # 返回新建部门类
