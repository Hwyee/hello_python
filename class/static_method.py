# 静态方法
class Static:
    def __init__(self, name, age, sex) -> None:
        self.name = name
        self.age = age
        self.sex = sex

    @staticmethod
    def get_name():
        return "static name"

    @staticmethod
    def get_age():
        return "static age"

    @staticmethod
    def get_sex():
        return "static sex"

    @staticmethod
    def get_all():
        return "static all"

    @staticmethod
    def get_all_class():
        return "static all class"

    @staticmethod
    def param(a):
        """
        没有内置参数，需要自己传参
        """
        return a.name


"""
静态方法：
    1.静态方法不需要实例化。不需要self参数。通过类名直接调用
    2.静态方法不能访问类属性，不能访问实例属性，不能访问类方法，不能访问实例方法
    3.静态方法不能修改类属性，不能修改实例属性，不能修改类方法，不能修改实例方法
    4.静态方法不能访问私有属性，不能访问私有方法
    5.静态方法不能访问私有变量，不能访问私有方法
"""

s = Static("python", 18, "male")
print(s.param(s))
