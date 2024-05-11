# 类
class ClassConcept:
    pass


"""
两种写法一样，默认继承的就是object,python可以多继承
class ClassConcept(object):
    pass
"""

# 实例化
cc = ClassConcept()
print(cc)
print(type(cc))
print(isinstance(cc, ClassConcept))
print(isinstance(cc, object))  # 所有的类都是object的子类
