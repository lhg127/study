import yaml
from selenium import webdriver
from time import sleep


class TestWeb:
    def setup(self):
        # 复用浏览器：先在终端输入命令"chrome --remote-debugging-port=9222"，打开浏览器，在复用浏览器的基础上 手动登录企业微信进入首页，
        web = webdriver.ChromeOptions()
        web.debugger_address = "127.0.0.1:9222"
        self.driver = webdriver.Chrome(options=web)
        self.driver.implicitly_wait(5)

    def teardown(self):
        sleep(3)
        self.driver.quit()
    #
    def test_web_driver(self):
        # 在首页进行菜单切换
        self.driver.find_element_by_id("menu_contacts").click()
        # 获取当前浏览器的cookie
        cook = self.driver.get_cookies()
        with open("./cook_data.yaml", "w", encoding="utf-8") as f:  # 将cook存入yaml文件中
            yaml.dump(cook, f)

    def test_cookie(self):
        # 实列化driver
        self.driver = webdriver.Chrome()
        # 登陆后的链接
        self.driver.get("https://work.weixin.qq.com/wework_admin/loginpage_wx?from=myhome")

    def test_cookies_web(self):
        # 扫码登录链接
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#apps")
        with open("cook_data.yaml", encoding='utf-8') as f:  # 打开yaml文件 并遍历拿到cookie
            data_cookie = yaml.safe_load(f)
            for cookie in data_cookie:
                self.driver.add_cookie(cookie)  # 将遍历的data_cookie值给cookie
        # 下面这个要写在for循环体外面，不然在连续的切换
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#manageTools")

# 如果不使用复用浏览器，那么每次都会重新打开浏览器，就无法获取到cookie绕过扫码登录
