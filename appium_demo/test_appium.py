from time import sleep

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy


class TestAppium:
    def setup_class(self):
        caps = {
            'platformName': 'Android',
            'deviceName': '127.0.0.1:7555',
            'platformVersion': '6.0.1',
            'appPackage': 'com.tencent.wework',
            'appActivity': '.launch.WwMainActivity',
            'noReset': True
        }
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', caps)
        self.driver.implicitly_wait(10)

    def teardown_class(self):
        pass
        # #sleep(2)
        # self.driver.quit()

    def test_app(self):
        sleep(6)
        # 切换到通讯录
        self.driver.find_element(MobileBy.XPATH, "//*[@text='通讯录']").click()
        # #点击添加成员
        self.driver.find_element(MobileBy.XPATH, "//*[@text='添加成员']").click()
        # 点击收到输入添加
        self.driver.find_element(MobileBy.XPATH, "//*[@text='手动输入添加']").click()
        # 输入姓名
        self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/ays").send_keys("测试")
        # 切换到电话输入框
        self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/f4m").click()
        # 输入电话号码
        self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/f4m").send_keys("13626636182")
        # 点击保存
        self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/ac9").click()
        # 点击返回到通讯录页
        self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/h86").click()
        sleep(2)
        # 保存完后判断页面是否在通讯录页面
        elem = self.driver.find_element(MobileBy.XPATH, "//*[@text='通讯录']")
        assert "通讯录" == elem.text
