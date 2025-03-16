# -*- coding: utf-8 -*-
"""
 raise 抛出异常

"""
class MyError(Exception):
    """_summary_ of an exception

    Args:
        Exception (_type_): _description_
    """
    def __init__(self, value):
        self.value = value

    def __str__(self):
        # repr()函数返回一个字符串，该字符串是对象的“官方”字符串表示形式。
        return repr(self.value)


try:
    raise MyError(2 * 2)
except MyError as e:
    print("My exception occurred, value:", e.value)
except (ArithmeticError,AttributeError) as e:
    print("Exception occurred, value:", e)
