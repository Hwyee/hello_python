""" range函数 range(start, stop, step),起始值默认为0，步长默认为1，生成一个等差序列，迭代器"""
# 序列是不可变的，不能修改，不能相加，相乘
print(range(1, 10))  # range(1, 10)
print(list(range(1, 10)))  # [1, 2, 3, 4, 5, 6, 7, 8, 9]

for i in range(1, 10):
    print(i)
