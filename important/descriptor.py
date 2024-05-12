# 描述器
class Descriptor:
    def __get__(self, obj, objtype):
        return "Madara"


class A:
    name = Descriptor()


a = A()
print(a.__dict__)
print(a.name)
a.name = "Naruto"
print(a.name)
Descriptor.__set__ = lambda: None  # 无意义的函数
print(a.name)
"""
函数输出：
{}
Madara
Naruto
Madara

"""
