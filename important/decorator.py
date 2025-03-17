"""装饰器
    需要返回一个被装饰的函数
"""

import time


def dec(f):
    """_summary_

    Args:
        f (_type_): _description_
    """
    print("dec(f)")
    print(type(f))
    return f


@dec
def test():
    """_summary_"""
    print("Testing")


# 完全等价于 dec(test)
print("Testing 其实解释器执行到@dec时就会调用dec(test)")
print(type(dec))
print("*****")
test()

def timeit(f):
    """_summary_

    Args:
        f (_type_): _description_
    """

    def wrapper(*args, **kwargs):
        start = time.time()
        print(type(f))
        end = time.time()
        print(f"took {end - start} seconds ")

    return wrapper


@timeit
def test1():
    """_summary_

    Returns:
        _type_: _description_
    """
    time.sleep(1)
    return 1


test1()  # took 1.0020806789398193 seconds
"""
@timeit(10)
def test():
    time.sleep(1)
    return 1
等价于
test = timeit(10)(test)
"""


# class装饰器
class Timer:
    """_summary_"""

    def __init__(self, f):
        self.f = f

    def __call__(self, *args, **kwargs):
        """
        这个方法表示,类和实例都是可调用的
        """
        start = time.time()
        ret = self.f(*args, **kwargs)
        end = time.time()
        print(f"took {end - start} seconds ")
        return ret


@Timer
def add(a, b):
    """_summary_

    Args:
        a (_type_): _description_
        b (_type_): _description_

    Returns:
        _type_: _description_
    """
    return a + b


# 等价于
# add = Timer(add)

print(add(2, 3))
"""
函数返回
took 0.0 seconds
5
@Timer(prefix=10)
def add(a, b):
    return a + b
add = Timer(prefix=10)(add)
"""
