"""类"""


class ClassConcept:
    """ 类定义，类名首字母大写
    """

    pass


class ClassConcept1(object):
    """
    两种写法一样，默认继承的就是object,python可以多继承

    """

    pass


# 实例化
cc = ClassConcept()
print(cc)
print(type(cc))
print(isinstance(cc, ClassConcept))
print(isinstance(cc, object))  # 所有的类都是object的子类
