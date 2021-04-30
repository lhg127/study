from faker import Faker


class Get_Fake:
    def __init__(self):
        self.faker = Faker('zh-CN')

    def get_name(self):
        name = self.faker.name()
        return name

    def get_number(self):
        iphones = self.faker.phone_number()
        return iphones
