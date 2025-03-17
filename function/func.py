"""函数使用

Returns:
    _type_: _description_
"""

import sys

print(sys.path)


# 函数的定义
def say_hello():
    """_summary_"""
    print("hello world")


say_hello()


# 带参数的函数
def say_hello1(name):
    """_summary_

    Args:
        name (_type_): _description_
    """
    print("hello", name)


say_hello1("python")
say_hello1("java")
say_hello1("c++")


# 带返回值的函数
def add(a, b):
    """_summary_

    Args:
        a (_type_): _description_
        b (_type_): _description_

    Returns:
        _type_: _description_
    """
    return a + b


print(add(1, 2))
print(add(2, 3))
print(add(3, 4))


# 带默认参数的函数
def say_hello(name="python"):
    """默认参数

    Args:
        name (name, optional): 名字. Defaults to "python".
    """
    print("hello", name)


say_hello()
say_hello("java")
say_hello("c++")

# 默认参数必须放到后面
# def say_hello(name="python", age):
# 错误 SyntaxError: parameter without a default follows parameter with a default
#    print("hello", name, age)


# 如果有多个默认参数 可以直接指定默认参数的值
def say_hello(name="python", age=18):
    """多个默认参数

    Args:
        name (str, optional): _description_. Defaults to "python".
        age (int, optional): _description_. Defaults to 18.
    """
    print("hello", name, age)


say_hello(age="world")


# 带可变参数的函数
def say_hello10(*names):
    """可变参数 会被封装成元组类型"""
    print(type(names))  # <class 'tuple'>
    for name in names:
        print("hello", name)


say_hello10("python")
say_hello10("java", "c++")
say_hello10("python", "java", "c++")

# say_hello(["python", "java", "c++"]) # say_hello() takes 0 positional arguments but 1 was given
say_hello10(
    *["python", "java", "c++"]
)  # 如果想传列表 需要使用 * 这是解包操作,**是解包字典的


# 可变参数 key values
def say_hello11(**names):
    """可变参数 kv形式"""
    print(type(names))
    for k, v in names.items():
        print("hello", k, v)


# say_hello({"name": "python", "age": 18})
# TypeError: say_hello() takes 0 positional arguments but 1 was given
say_hello11(**{"name": "python", "age": 18})  # 如果想传字典 需要使用 **


# 递归函数
def fact(n):
    """_summary_

    Args:
        n (_type_): _description_

    Returns:
        _type_: _description_
    """
    if n == 1:
        return 1
    else:
        return n * fact(n - 1)


print(fact(5))
