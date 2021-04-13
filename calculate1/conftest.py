import pytest
import yaml
from calculate1.calcul import Operation


# 初始化计算
@pytest.fixture(scope="class")
def get_cal():
    cal = Operation()  # 类实例化对象
    yield cal
    print("计算结束")


# 取到yaml数据并返回给data
def data():
    with open("../calculate1/data.yaml")as get:
        get_yaml = yaml.safe_load(get)
        return get_yaml


# 加法参数化
@pytest.mark.run(order=4)
@pytest.fixture(params=data()['ints_add'], ids=data()['ids'])
def add(request):
    return request.param  # 将数据返回给add


# 减法参数化
@pytest.fixture(params=data()["subts"], ids=data()["sub_ids"])
def subt(request):
    return request.param


# 乘法参数化
@pytest.fixture(params=data()["mul"], ids=data()["mul_ids"])
def mult(request):
    return request.param


# 除法参数化
@pytest.fixture(params=data()["div"], ids=data()["div_ids"])
def div(request):
    return request.param

#
# def pytest_collect_modifyitems(session,config,items:list):
#     print("这是收集所有测试用")
#     print(items)
