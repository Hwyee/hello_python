"""
class_super.py
"""


class A:
    """_summary_"""

    def __init__(self, age) -> None:
        self.age = age


class B(A):
    """_summary_

    Args:
        A (_type_): _description_
    """

    def __init__(self, age, name) -> None:
        super().__init__(age)
        self.name = name


class C(B):
    """_summary_

    Args:
        B (_type_): _description_
    """

    def __init__(self, age, name) -> None:
        # 等价于 super(C, self).__init__(age,name)
        # 就是寻找C的父类方法，按照self类的搜索的顺序
        # super().__init__(age,name)
        super(B, self).__init__(age)  # 这里调用的是A的构造方法
        self.sex = "male"


c = C(18, "cfire")
print(c.__dict__)  # {'age': 18, 'sex': 'male'} 没有name属性
super(C, c).__init__(c.age, "cfire")  # 调用B的构造方法
print(c.__dict__)  # {'age': 18, 'sex': 'male', 'name': 'cfire'}
