# 元组 元组的元素不可以修改，但是可以添加删除元素
t = ("a", 2, True, 3.14, "e")
print(t)
print(t[0])
print(t[1:3])

# tuple如果只有一个元素，则需要加逗号
t1 = ("a",)
print(t1)

# 如果不加逗号，则t2是一个字符串，此时这个括号被看成算数运算符的括号
t2 = "a"
print(t2)
print(type(t2))

# 如果是空元组
t3 = ()
print(t3)
print(type(t3))
t4 = tuple()
print(t4)
print(type(t4))

# string to tuple
s = "abcde"
t5 = tuple(s)
print(t5)
print(type(t5))


# 内置函数
t6 = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(len(t6))
print(max(t6))
print(min(t6))
print(sum(t6))
t6 = (1, 2)
# del t6[0] TypeError: 'tuple' object doesn't support item deletion
del t6
# print(t6) NameError: name 't6' is not defined

# tuple to 加法
t7 = (1, 2, 3)
t8 = t7 + (4, 5, 6)
print(t8)

# 元素不可修改
# t7[0] = 111 # TypeError: 'tuple' object does not support item assignment
print(t7)

# 元组的常用方法
t9 = (1, 2, 3, 4, 5, 1, 7, 8, 1, 10)
print(t9.count(1))  # 3 统计元素出现的次数
print(t9.index(1))  # 0 返回该值的第一个索引

# 遍历元组
for i in t9:
    print(i, end=" ")
print()
for i in range(len(t9)):
    print(t9[i], end=" ")
print()
for i, j in enumerate(t9):
    print(i, j)
