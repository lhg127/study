import yaml
from selenium import webdriver


class BasePage:
    def __init__(self, base_page=None):  # 构造方法实现重复打开浏览器问题
        if base_page == None:
            self.driver = webdriver.Chrome()

            self.driver.get("https://work.weixin.qq.com/wework_admin/loginpage_wx?")
            self.driver.implicitly_wait(3)
            with open("../base_page/cook_data.yaml", encoding="utf-8") as f:
                cookies = yaml.safe_load(f)
                for cook in cookies:
                    self.driver.add_cookie(cook)
                self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        else:
            self.driver = base_page

    # def find(self, by, ele=None):  # 封装find_element
    #     if ele == None:
    #
    #         return self.driver.find_element_by(*by)
    #     else:
    #         return self.driver.find_element_by(by, ele)
