"""生成器

"""
 


def reverse(data):
    """_summary_

    Args:
        data (_type_): _description_

    Returns:
        _type_: _description_

    Yields:
        _type_: _description_
    """
    for index in range(len(data) - 1, -1, -1):
        yield data[index]
    return 100


a = reverse("abcde")
while True:
    try:
        print(next(a))
    except StopIteration as e:
        print(e.value)
        break


print(
    "-----------------------------send()------------------------"
)


# send 方法
def gen():
    """_summary_

    Yields:
        _type_: _description_
    """
    x = 0
    while x < 10:
        received_value = yield x
        print("received_value:{%s}" % received_value)
        if received_value is not None:
            x = received_value
        else:
            x += 1


g = gen()
# send方法,如果传递的是非None值，则不能在next之前调用，需要调用一次next方法
# print(g.send(100))  # TypeError: can't send non-None value to a just-started generator
print(g.send(None))  # 输出：0 这样可以，其实next底层也是调用的send(None)
print(next(g))  # 输出：1
print(next(g))  # 输出：2
print(next(g))  # 输出：3
print(g.send(5))  # send方法将值发送到 received_value = 10

for i in g:
    print(i)
# print(g.send(None)) # StopIteration:




# yield from
def outer_generator():
    """
    一个简单的生成器函数，用于生成从0到1的整数序列。

    Yields:
        int: 当前生成的整数值。
    """
    for k in range(3):
        print(f"**{k}**")
        yield from inner_generator()


def inner_generator():
    """
    一个简单的生成器函数，用于生成从0到1的整数序列。

    Yields:
        int: 当前生成的整数值。
    """
    # yield 0
    # yield 1
    yield from range(2)
    # for j in range(2):
    #     yield j


gen = outer_generator()
print(
    "-----------------yield from-------------------------"
)
print(next(gen))  # 输出：**0** 0
print(next(gen))  # 输出：1
print(next(gen))  # 输出：0
print(next(gen))  # 输出：1
print(next(gen))  # 输出：0
print(next(gen))  # 输出：1
