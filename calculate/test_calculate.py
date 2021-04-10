import pytest
import yaml
from calculate.calculates import Operation


# @pytest.mark.parametrize("a,b,exper", yaml.safe_load(open("../data/datas.yaml")))
class TestCalculate:
    def setup_class(self):
        self.cal = Operation()
        print("前置准备")

    def teardown_class(self):
        print("结束测试")

    # def setup(self):
    #     self.cal = Operation()
    #     print("前置准备")
    #
    # def teardown(self):
    #     print("结束测试")

    @pytest.mark.parametrize("a,b,expect", [[1, 1, 2], [1, 5, 6]], ids=["add_1", "add_2"])
    def test_add(self, a, b, expect):
        assert expect == self.cal.add(a, b)
        print("加法")

    @pytest.mark.parametrize("a,b,expect", [[10, 5, 5], [6, 4, 2]], ids=["subt_1", "subt_2"])
    def test_subt(self, a, b, expect):
        assert expect == self.cal.subt(a, b)
        print("减法")

    @pytest.mark.parametrize("a,b,expect", [(2, 6, 12), (3, 6, 18)], ids=["mult_1", "mult_2"])
    def test_mult(self, a, b, expect):
        assert expect == self.cal.mult(a, b)
        print("乘法")

    @pytest.mark.parametrize("a,b,expect", [(0.6, 2, 3), (0, 2, 0)], ids=["div_1", "div_2"])
    def test_div(self, a, b, expect):
        assert expect == round(self.cal.div(a, b))
        print("除法")
