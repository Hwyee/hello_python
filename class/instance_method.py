"""
实例方法
"""


class Ice:
    """
    没有装饰器的第一个参数一定是实例对象,一般用self表示
    比如@staticmethod @classmethod 第一个参数不是self
    """

    madara = 1

    def __init__(self, a, b, c) -> None:
        self.a = a
        self.b = b
        self.c = c

    def get_a(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        return self.a

    def get_b(self):
        """获取b

        Returns:
            int: b
        """
        return self.b

    def get_c(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        return self.c


ice = Ice(1, 2, 3)
print(ice.get_a())
print(ice.get_b())
print(ice.get_c())


class MyClass:
    """普通方法"""

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def my_function(arg1, arg2):  # 这是一个普通函数，没有 `self` 或 `cls`
        """_summary_

        Args:
            arg1 (_type_): _description_
            arg2 (_type_): _description_
        """
        print(f"普通 Function called with {arg1} and {arg2}")


# 通过类名调用普通函数普通函数​（在类中定义但没有绑定到实例或类的函数）
# ​只能通过类名调用，而不能通过实例调用。这是因为普通函数没有绑定到实例或类，
# Python 不会自动将实例作为第一个参数传递给它。
MyClass.my_function("Hello", "World")  # 输出: Function called with Hello and World

mc = MyClass(1, 2, 3)
# 通过实例调用普通函数 第一个参数如果不是实例会报错
# mc.my_function("Hello", "World")

# 普通 Function called with
# <__main__.MyClass object at 0x000001146AC7A210> and hhhhh
mc.my_function("hhhhh")
