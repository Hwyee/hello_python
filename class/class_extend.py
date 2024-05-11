# 继承
class A:
    def __init__(self, name, age, sex) -> None:
        self.name = name
        self.age = age
        self.sex = sex

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def get_sex(self):
        return self.sex

    def get_all(self):
        return self.name, self.age, self.sex


class B(A):
    pass


class C(A):
    def __init__(self, name, age, sex, height) -> None:
        super().__init__(name, age, sex)
        self.height = height

    def get_height(self):
        return self.height


a = A("a", 1, "male")
b = B("b", 2, "female")
c = C("c", 3, "male", 180)
print(a.get_all())
print(b.get_all())
print(c.get_all(), c.get_height())
