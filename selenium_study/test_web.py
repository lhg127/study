import yaml
from selenium import webdriver
from time import sleep


class Testdrive:
    # 不使用复用浏览器，打开扫码页
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://work.weixin.qq.com/wework_admin/loginpage_wx?")
        self.driver.implicitly_wait(5)

    # 调试使用
    # def setup(self):
    #     opt = webdriver.ChromeOptions()
    #     opt.debugger_address = "127.0.0.1:9222"
    #     self.driver = webdriver.Chrome(options=opt)
    #     self.driver.implicitly_wait(5)

    def teardown(self):
        sleep(3)
        self.driver.quit()

    def test_web(self):
        # 不用复用浏览器进行登录， 好处就是不用一直开着浏览器，任意浏览器都可以使用，但必须更新不同浏览器cookie才能使用
        with open("cook_data.yaml", encoding="utf-8") as f:
            cookie = yaml.safe_load(f)
            for cook in cookie:
                self.driver.add_cookie(cook)
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        # 切换到通讯录
        self.driver.find_element_by_id("menu_contacts").click()
        # 输入用户名
        self.driver.find_element_by_link_text("添加成员").click()  # 添加成员使用xpath定位到有8个a标签元素，就是定位不到第一个元素？
        self.driver.find_element_by_id("username").send_keys("企业微信注册")
        # 输入别名
        self.driver.find_element_by_id("memberAdd_english_name").click()
        self.driver.find_element_by_id("memberAdd_english_name").send_keys("企鹅")
        # 输入账号
        self.driver.find_element_by_id("memberAdd_acctid").click()
        self.driver.find_element_by_id("memberAdd_acctid").send_keys("123456")
        # 选择性别
        self.driver.find_element_by_class_name("ww_radio").click()
        # 输入电话号码
        self.driver.find_element_by_id("memberAdd_phone").click()
        self.driver.find_element_by_id("memberAdd_phone").send_keys("13026636182")
        # 保存添加
        self.driver.find_element_by_partial_link_text("保存并继续添加").click()
