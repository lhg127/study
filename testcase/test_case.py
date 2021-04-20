from pageobject.home_page import Homepage
from selenium import webdriver
import pytest


class TestAddDepartment:
    def setup_class(self):
        self.page = Homepage()  # 实列化Homepage

    def teardown(self):


    @pytest.mark.parametrize("name", [("测试")])  # 数据分离出来进行参数化
    def test_add_department(self, name):
        # 1、跳转到通讯页      2、添加部门                 3、跳转到新建部门弹窗页
        list_ele = self.page.home_page().click_add_department().add_department(name)
        assert name in list_ele  # 断言结果
