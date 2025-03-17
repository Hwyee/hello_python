"""
封装

"""


class A:
    """_summary_"""

    def __init__(self, name, age, sex, doom) -> None:
        self.name = name
        self._age = age  # 受保护的属性
        self.__sex = sex  # 私有属性
        self.__doom__ = doom

    def _get_sex(self):
        return self.__sex

    @property  # 属性装饰器 把函数调用改成属性调用
    def sex(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        return self.__sex

    @sex.setter  # 变量修改装饰器 函数名要和property装饰器同名
    def sex(self, sex):
        self.__sex = sex

    @sex.deleter
    def d_sex(self):  # 删除装饰器 名字不需要和属性装饰器同名
        del self.__sex
        print(self.__get_doom())

    def __get_doom(self):  # 私有方法
        return self.__doom__

    def test(self):
        """_summary_
        """
        print(A.testAttr)

    testAttr = 1


a = A("python", 18, "male", "doom")
print(a.name)
print(a._age)  # 受保护的属性 口头约定 不想被别人访问 但是可以访问
# print(a.__sex) AttributeError: 'A' object has no attribute '__sex'     # 私有属性 不能被访问 访问不到

print(a.__doom__)  # 可以访问

print(a._get_sex())
# print(a.__get_doom()) # AttributeError: 'A' object has no attribute '__get_doom'

print(
    a.__dict__
)  # {'name': 'python', '_age': 18, '_A__sex': 'male', '__doom__': 'doom'}

# 私有属性为什么访问不到是因为底层给你改名字了 这个_A__sex就是__sex属性
print(a._A__sex)  # male

print(dir(a))  # 打印属性和方法
# 方法也是一样
print(A.__dict__)
# {'__module__': '__main__', '__init__': <function A.__init__ at 0x0000018B70E15260>,
# '_get_sex': <function A._get_sex at 0x0000018B70E174C0>,
# '_A__get_doom': <function A.__get_doom at 0x0000018B70E14D60>,
# '__dict__': <attribute '__dict__' of 'A' objects>,
# '__weakref__': <attribute '__weakref__' of 'A' objects>, '__doc__': None}

print(a._A__get_doom())


print("*" * 30 + "装饰器" + "*" * 30)
# 属性装饰器
print(a.sex)
print(type(a.sex))
# print(a.sex()) # TypeError: 'str' object is not callable
a.sex = "sssss"
print(a.sex)
del a.d_sex
# print(a.sex)  # AttributeError: 'A' object has no attribute '_A__sex'
a.test = 2
# a.test() # TypeError: 'int' object is not callable

print(type(property))
