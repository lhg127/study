from selenium.webdriver.common.by import By

from base_page.basepage import BasePage
from time import sleep


class AddDepartment(BasePage):  # 新建部门类
    # 元素分离出来并私有化
    __send_name = "name"
    __add_elem = "js_parent_party_name"
    __select_elem = ".qui_dialog_body.ww_dialog_body [id='1688851348010191_anchor']"
    __click_elem = "确定"
    __css = (By.CSS_SELECTOR, '.jstree-anchor')

    def add_department(self, name):  # 新建部门弹窗页
        self.driver.find_element_by_name(self.__send_name).send_keys(name)  # 输入用户名
        self.driver.find_element_by_class_name(self.__add_elem).click()  # 点击所属部门
        sleep(3)
        self.driver.find_element_by_css_selector(self.__select_elem).click()  # 选择部门难点,使用组合定位
        self.driver.find_element_by_link_text(self.__click_elem).click()  # 点击确定
        sleep(3)  # 需要给等待时间，要不会报错
        els = self.driver.find_elements(*self.__css)  # 注意点容易写element，一直定位不到
        list_ele = []
        for element in els:
            list_ele.append(element.text)
            print(list_ele)

        return list_ele  # 返回结果给testcase进行断言
