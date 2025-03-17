"""变量作用域"""

# 全局变量
A = 10


def say_hello():
    """_summary_"""
    print("hello")
    print(A)


say_hello()


# 局部变量
def say_hellolocal():
    """_summary_"""
    b = 10
    print("hello")
    print(b)


say_hellolocal()

# print(b) # 报错 NameError: name 'b' is not defined


def say_hellol2():
    """_summary_"""
    A = 100  # 局部变量
    print("hello")
    print(A)


say_hellol2()
print(A)  # 10


# 函数中操作全局变量
def say_helloglobal():
    """全局变量"""
    global A  # 声明操作的是全局变量
    A = 100
    print("hello")
    print(A)


say_hello()
print(A)


# nonlocal 操作上个作用域上的变量,非全局
def say_nonlocal():
    """nolocal"""
    # nonlocal A 不能修改全局变量
    nl = 20
    nl2 = 88

    def say_n2():
        nonlocal nl
        nl = 30
        print(nl)

        def say_n3():
            nonlocal nl
            nonlocal nl2
            print(nl) # 修改的是say_n2的nl
            nl = 40
            print(nl)
            print("say_n3 ")
            print(nl2)
            nl2 = 99
            print(nl2)

        say_n3()

    say_n2()

print("****************nonlocal****************")
say_nonlocal()
