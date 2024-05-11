# 实例方法
class Ice:
    madara = 1
    """
    没有装饰器的第一个参数一定是实例对象,一般用self表示
    
    """

    def __init__(self, a, b, c) -> None:
        self.a = a
        self.b = b
        self.c = c

    def get_a(self):
        return self.a

    def get_b(self):
        return self.b

    def get_c(self):
        return self.c


ice = Ice(1, 2, 3)
print(ice.get_a())
print(ice.get_b())
print(ice.get_c())
