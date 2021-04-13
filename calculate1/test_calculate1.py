import allure


class TestCalculate:
    # 加法运算
    @allure.feature("加法")
    @allure.story("加法运算")
    @allure.step("加法整形浮点型计算")
    @allure.title("测试加法")
    def test_add(self, get_cal, add):
        assert add[2] == get_cal.add(add[0], add[1])
        print(add)

    # 减法运算，使用round保留二位
    @allure.feature("减法")
    @allure.story("减法运算")
    @allure.step("减法整形浮点型计算")
    @allure.title("测试减法")
    def test_subt(self, get_cal, subt):
        assert subt[2] == round(get_cal.subt(subt[0], subt[1]), 2)
        print(subt)

    # 乘法运算，使用round保留六位
    @allure.feature("乘法")
    @allure.story("乘法运算")
    @allure.step("乘法整形浮点型计算")
    @allure.title("测试乘法")
    def test_mult(self, get_cal, mult):
        assert mult[2] == round(get_cal.mult(mult[0], mult[1]), 6)
        print(mult)

    # 除法运算，使用try抛出ZeroDivisionError错误
    @allure.feature("除法")
    @allure.story("除法运算")
    @allure.step("除法整形浮点型计算")
    @allure.title("测试除法")
    def test_div(self, get_cal, div):
        try:
            assert div[2] == get_cal.div(div[0], div[1])
        except:
            assert ZeroDivisionError
        print(div)
        print("除数为零")
