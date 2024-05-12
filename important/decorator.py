# 装饰器
def dec(f):
    pass


@dec
def test():
    pass


# 完全等价于
test = dec(test)

import time


def timeit(f):
    def wrapper(*args, **kwargs):
        start = time.time()
        f()
        end = time.time()
        print(f"took {end - start} seconds ")

    return wrapper


@timeit
def test():
    time.sleep(1)
    return 1


test()  # took 1.0020806789398193 seconds
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
