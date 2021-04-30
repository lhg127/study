from wechat.homepage import HomePage
from wechat.fake import Get_Fake
from wechat.app import StartApp


class TestWechat:
    def setup_class(self):
        # 实列化HomePage
        self.page = HomePage()
        # 实例化Gte_fake
        self.get_faker = Get_Fake()
        # # 实列化StartApp
        self.start = StartApp()

    def setup(self):
        #   启动app，只是在启动欢迎页
        self.start.startapp()
        # 需要新建一个main函数返回到homepage页
        self.mian = self.start.mian_a()

    def teardown(self):
        # 关闭app
        self.start.restartapp()

    def teardown_class(self):
        # 关闭driver
        self.start.stopapp()

    # 用例一
    def test_addmember(self):  # 添加成员
        name = self.get_faker.get_name()
        iphones = self.get_faker.get_number()
        # 切换到通讯录页            # 点击添加成员         # 点击手动输入添加    # 编辑添加成员    # 点击返回通讯录页
        self.page.goto_contact().click_add_member().click_eadit_add().eadit_contact(name, iphones).back_addmember()

    # 用例二
    def test_delete_member(self):  # 删除成员
        # 切换到通讯录页            # 点击编辑        #选择成员        #删除成员        #返回通讯录页
        self.mian.goto_contacts().click_editor().select_member().delete_member().back_contacts()
