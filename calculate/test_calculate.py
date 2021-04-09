import pytest
import yaml


#@pytest.mark.parametrize("a,b", yaml.safe_load(open("../data/datas.yaml")))
class TestCalculate:

    def test_add(self, a, b):
        assert 16 == a + b
        print("加法")

    def test_subt(self, a, b):
        assert 4 == a - b
        print("减法")

    @pytest.mark.parametrize("a,b", [(2, 6), (3, 4)])
    def test_mult(self, a, b):
        assert 12 == a * b
        print("乘法")

    @pytest.mark.parametrize("a,b", [(0.6, 0.2), (7, 2)])
    def test_div(self, a, b):
        assert 3 == round(a / b)
        print("除法")
