"""
类属性
"""


class Ice:
    """
    Ice doc
    """

    madara = 1  # 类属性

    def __init__(self, a, b, c) -> None:
        """
        初始化函数
        """
        self.a = a
        self.b = b
        self.c = c
        Ice.madara += 100

    def get_a(self):
        """
        获取a
        """
        return self.a

    def get_b(self):
        """
        获取b
        """
        return self.b


ice = Ice(1, 2, 3)

print(ice.madara)  # 101
print(ice.__dict__)  # 没有打印类属性
print(Ice.__dict__)  # 打印类属性,和类方法 101

# 类属性相当于静态变量吧
