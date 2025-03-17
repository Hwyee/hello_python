# 匿名函数
""" 匿名函数，即没有函数名称的函数，这种函数称为匿名函数。
# 匿名函数的语法格式如下：
# lambda [arg1 [,arg2,.....argn]]:expression
# lambda函数的参数列表和普通函数一样，只是没有函数名。
# lambda函数的表达式部分和普通函数的return语句一样，只是没有return关键字。
# lambda函数的参数列表和表达式部分用冒号分隔。
"""

lambda x, y: x + y
# 调用匿名函数
print((lambda x, y: x + y)(1, 2))
# 也可以给匿名函数起个名字
add = lambda x, y: x + y
print(add(1, 2))

# map函数 迭代器
list1 = [1, 2, 3, 4, 5]
list2 = map(lambda x: x * 2, list1)
print(list2)
print(list(list2))


# filter函数
list1 = [1, 2, 3, 4, 5]
list2 = filter(lambda x: x % 2 == 0, list1)
print(list2)
print(list(list2))

# reduce函数 累积函数
from functools import reduce

list1 = [1, 2, 3, 4, 5]
list2 = reduce(lambda x, y: x + y, list1)
print(list2)
