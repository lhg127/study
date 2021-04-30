from appium import webdriver
from BasePage.basepage import Start_app


class StartApp(Start_app):
    # 启动app
    def startapp(self):
        if self.driver is None:
            caps = {}
            caps["platformName"] = "android"
            caps["platformVersion"] = "6.0.1"
            caps["deviceName"] = "127.0.0.1:7555"
            caps["appPackage"] = "com.tencent.wework"
            caps["appActivity"] = ".launch.WwMainActivity"
            caps["dontStopAppOnReset"] = "true"  # 在使用adb启动应用程序之前，不要停止被测应用程序的进程
            caps["noReset"] = "true"
            self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)
            self.driver.implicitly_wait(15)
        else:
            # 复用启动app
            self.driver.launch_app()

    def restartapp(self):
        # 关闭app，只是挂于后台
        self.driver.close_app()

    def stopapp(self):
        # 关闭driver
        self.driver.quit()

    def mian_a(self):
        # 局部导入
        from wechat.homepage import HomePage
        # 返回HomePage页
        return HomePage(self.driver)
