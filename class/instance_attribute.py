# 实例属性
class Via:
    pass


v = Via()
v.a = 1
print(v.a)


class Ace:
    """
    ace doc
    """

    def __init__(self, a, b, c) -> None:
        """
        初始化函数
        """
        self.a = a # 实例属性
        self.b = b
        self.c = c

    def get_a(self):
        """
        获取a
        """
        return self.a


ace = Ace(1, 2, 3)
print(ace.get_a())
# ac = Ace() TypeError: Ace.__init__() missing 3 required positional arguments: 'a', 'b', and 'c'
print(ace.__dict__)  # {'a': 1, 'b': 2, 'c': 3}
print(ace.__class__)  # <class '__main__.Ace'>
print(ace.__doc__)
