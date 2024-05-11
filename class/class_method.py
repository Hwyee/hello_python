# 类方法
class Fire:
    cname = "cfire"
    cage = 999
    csex = "cmale"

    def __init__(sel, name, age, sex) -> None:
        sel.name = name
        sel.age = age
        sel.sex = sex

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def get_sex(self):
        return self.sex

    def get_all(self):
        return self.name, self.age, self.sex

    @classmethod
    def get_all_class(cls):
        """
        classmethod:
        classmethod的调用方式
        1. 类名.方法名()
        2. 类名().方法名()
        3. 对象名.方法名()

        第一个参数是类对象,一般用cls表示,cls.cname, cls.cage, cls.csex
        """
        return cls.cname, cls.cage, cls.csex


f = Fire("fire", 18, "male")
print(f.get_all())
print(f.get_all_class())
print(Fire.get_all_class())
# print(Fire.get_all()) # TypeError: Fire.get_all() missing 1 required positional argument: 'self'
print(Fire.get_all(f))
