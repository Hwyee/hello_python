# 变量作用域
# 全局变量
a = 10


def say_hello():
    print("hello")
    print(a)


say_hello()


# 局部变量
def say_hello():
    b = 10
    print("hello")
    print(b)


say_hello()

# print(b) # 报错 NameError: name 'b' is not defined


def say_hello():
    a = 100  # 局部变量
    print("hello")
    print(a)


say_hello()
print(a)  # 10


# 函数中操作全局变量
def say_hello():
    global a  # 声明操作的是全局变量
    a = 100
    print("hello")
    print(a)


say_hello()
print(a)
