"""random_use.py"""
import random

# 随机小数
print(random.random())
# 随机整数
print(random.randint(1, 10))  # 左闭右闭


# 随机获取列表元素
print(random.choice([1, 2, 3, 4, 5]))
print(random.choice("abcde"))


# 生成一个随机字母组成的列表
list1 = list("abcdefghijklmnopqrstuvwxyz")
print(random.choices(list1, k=5))
