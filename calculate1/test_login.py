import pytest


class Testlogin:
    # 创建输入方法执行顺序第三
    @pytest.mark.run(order=3)
    def test_input(self):
        print("输入搜索内容")

    # 创建登录方法执行顺序第一
    @pytest.mark.run(order=1)
    def test_login(self):
        print("登录账号")

    # 创建搜索方法执行顺序第二
    @pytest.mark.run(order=2)
    def test_search(self):
        print("打开搜索")
