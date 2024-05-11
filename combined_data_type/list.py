# 列表
list1 = [1, True, "hello", 3.14]
print(type(list1))
print(list1)
print(list1[0])
print(list1[-1])


# 类型转换 str -> list
list2 = list("hello")
print(list2)  # ['h', 'e', 'l', 'l', 'o']


"""
以下操作都会报错
list2 = list(1) TypeError: 'list' object is not callable
list2 = list(True) TypeError: 'bool' object is not iterable
"""

# 列表的切片
list3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(list3[0:5])  # [1, 2, 3, 4, 5]

# 列表相加
list4 = [1, 2, 3]
list5 = [4, 5, 6]
print(list4 + list5)  # [1, 2, 3, 4, 5, 6]

# 列表乘法
list6 = [1, 2, 3]
print(list6 * 3)  # [1, 2, 3, 1, 2, 3, 1, 2, 3]


# 列表元素查找
list7 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("1" in list7)  # False
print(1 in list7)  # True

# 大于小于等于
list8 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list9 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(list8 == list9)  # True
print(list8 > list9)  # False

# 列表内置函数  函数名()
list10 = [1, 2, 3, 4, 5, 6, 7, 10, 9, -1]
print(len(list10))
print(max(list10))
print(min(list10))
print(sum(list10))
print(sorted(list10))
del list10[0]
print(list10)
del list10
# print(list10) NameError: name 'list10' is not defined

print("*" * 30)

# 列表遍历
for i in list1:
    print(i)

# 枚举遍历 带有列表索引
for i, j in enumerate(list1):
    print(i, j)

# range() 遍历
for i in range(len(list1)):
    print(i, list1[i])

print("*" * 30)
# 列表的常用方法  变量名.方法名()
list1.append(11)  # 添加元素
print(list1)

list1.extend([12, 13, 14])  # 添加多个元素
print(list1)
list1.insert(0, 0)  # 插入元素
print(list1)

list1.pop(0)  # 删除元素 根据索引
print(list1)
list1.remove(11)  # 删除元素 根据值
print(list1)

list1.append(13)
list1.remove(13)  # 如果有多个元素，只会删除第一个
print(list1)

list1.clear()  # 清空列表
print(list1)
