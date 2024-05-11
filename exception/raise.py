# -*- coding: utf-8 -*-
# raise 抛出异常
class MyError(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)


try:
    raise MyError(2 * 2)
except MyError as e:
    print("My exception occurred, value:", e.value)
except Exception as e:
    print("Exception occurred, value:", e.value)
