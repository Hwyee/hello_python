# super
class A:
    def __init__(self, age) -> None:
        self.age = age


class B(A):
    def __init__(self, age, name) -> None:
        super().__init__(age)
        self.name = name


class C(B):
    def __init__(self, age, name) -> None:
        # super().__init__(age,name)# 等价于 super(C, self).__init__(age,name) 就是寻找C的父类方法，按照self类的搜索的顺序
        super(B, self).__init__(age)  # 这里调用的是A的构造方法
        self.sex = "male"


c = C(18, "cfire")
print(c.__dict__)  # {'age': 18, 'sex': 'male'} 没有name属性
super(C, c).__init__(c.age, "cfire")  # 调用B的构造方法
print(c.__dict__)  # {'age': 18, 'sex': 'male', 'name': 'cfire'}
