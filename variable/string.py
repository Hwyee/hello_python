# 字符串
str_1 = "1"
print(str_1)
str_2 = "1"
print(str_2)
str_3 = """
1
2
3
"""
print(str_3)

# 字符串加法
str_4 = "1" + "2"
print(str_4)
# s1 = 1+"" 报错TypeError: unsupported operand type(s) for +: 'int' and 'str'
# 字符串乘法
str_5 = "1" * 2
print(str_5)
# 字符串索引
str_6 = "123"
print(str_6[0])
print(str_6[-1])
# 切片 参数：[start:end:step]
print(str_6[0:2])  # 左闭右开
print(str_6[:2])
print(str_6[2:])
# 1:2:1 第三个参数是步数，默认是1
print(str_6[::2])  # 13
# 字符串反转
print(str_6[::-1])


print("*" * 20 + "序列的通用函数" + "*" * 20)
# 序列的通用函数
str_7 = "123abc)"
print(len(str_7))
print(max(str_7))
print(min(str_7))
print(sorted(str_7))
del str_7
# print(str_7) # 报错NameError: name 'str_7' is not defined

print("*" * 20 + "字符串的常用方法" + "*" * 20)
# 字符串的常用方法
str_8 = "a123abc"
print(str_8.capitalize())  # A123abc 首字母大写
print(str_8.count("a"))  # 2
print(str_8.find("a"))  # 0
print(str_8.index("a"))  # 0
print(
    str_8.isalnum()
)  # True 如果字符串中的所有字符都是字母数字并且 字符串中至少有一个字符。
print(str_8.islower())  # False
print(str_8.isupper())  # False

print("   aa  ".strip())  # aa

print("**".join("abc"))

print("*" * 20 + "字符串遍历" + "*" * 20)
str_9 = "123abc"
for i in str_9:
    print(i, end=" -*- ")
print()
for i in range(len(str_9)):
    print(str_9[i], end=" -*- ")
print()

for i in enumerate(str_9):
    print(i, type(i))
