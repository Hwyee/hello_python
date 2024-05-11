import sys

print(sys.path)


# 函数的定义
def say_hello():
    print("hello world")


say_hello()


# 带参数的函数
def say_hello(name):
    print("hello", name)


say_hello("python")
say_hello("java")
say_hello("c++")


# 带返回值的函数
def add(a, b):
    return a + b


print(add(1, 2))
print(add(2, 3))
print(add(3, 4))


# 带默认参数的函数
def say_hello(name="python"):
    print("hello", name)


say_hello()
say_hello("java")
say_hello("c++")

# 默认参数必须放到后面
# def say_hello(name="python", age): # 错误 SyntaxError: parameter without a default follows parameter with a default
#    print("hello", name, age)


# 如果有多个默认参数 可以直接指定默认参数的值
def say_hello(name="python", age=18):
    print("hello", name, age)


say_hello(age="world")


# 带可变参数的函数
def say_hello(*names):
    print(type(names))  # <class 'tuple'>
    for name in names:
        print("hello", name)


say_hello("python")
say_hello("java", "c++")
say_hello("python", "java", "c++")

# say_hello(["python", "java", "c++"]) # say_hello() takes 0 positional arguments but 1 was given
say_hello(*["python", "java", "c++"])  # 如果想传列表 需要使用 *


# 可变参数 key values
def say_hello(**names):
    print(type(names))
    for k, v in names.items():
        print("hello", k, v)


# say_hello({"name": "python", "age": 18}) # TypeError: say_hello() takes 0 positional arguments but 1 was given
say_hello(**{"name": "python", "age": 18})  # 如果想传字典 需要使用 **


# 递归函数
def fact(n):
    if n == 1:
        return 1
    else:
        return n * fact(n - 1)


print(fact(5))
