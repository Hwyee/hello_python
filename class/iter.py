"""
迭代器
iterable 可以迭代的 itertor 迭代器

"""

class Reverse:
    """Iterator for looping over a sequence backwards."""

    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        # 如果没有数据需要抛出StopIteration
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        return self.data[self.index]


rev = Reverse("spam")
a = iter(rev)

# 因为rev实现了__iter__和__next__方法，所以可以迭代
for i in rev:
    print(i)

rev1 = Reverse("abcc")
b = iter(rev1)
# iter()返回的是迭代器对象，所以可以迭代 但是这个操作需要实现 __iter__
for i in b:
    print(i)


# 比如 没有实现__iter__和__next__方法，那么这个对象无法迭代
class Reverse2:
    """Iterator for looping over a sequence backwards."""

    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __next__(self):
        # 如果没有数据需要抛出StopIteration
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        return self.data[self.index]


print(
    "----------------")
rr = Reverse2("reve")

# for i in rr: # TypeError: 'Reverse2' object is not iterable
#     print(i)

# for i in iter(rr): # TypeError: 'Reverse2' object is not iterable
#     print(i)
