""" 字符串 """
STR_1 = "1"
print(STR_1)
STR_2 = "1"
print(STR_2)
STR_3 = """
1
2
3
"""
print(STR_3)

# 字符串加法
STR_4 = "1" + "2"
print(STR_4)
# s1 = 1+"" 报错TypeError: unsupported operand type(s) for +: 'int' and 'str'
# 字符串乘法
STR_5 = "1" * 2
print(STR_5)
# 字符串索引
STR_6 = "123"
print(STR_6[0])
print(STR_6[-1])
# 切片 参数：[start:end:step]
print(STR_6[0:2])  # 左闭右开
print(STR_6[:2])
print(STR_6[2:])
# 1:2:1 第三个参数是步数，默认是1
print(STR_6[::2])  # 13
# 字符串反转
print(STR_6[::-1])


print("*" * 20 + "序列的通用函数" + "*" * 20)
# 序列的通用函数
STR_7 = "123abc)"
print(len(STR_7))
print(max(STR_7))
print(min(STR_7))
print(sorted(STR_7))
del STR_7
# print(STR_7) # 报错NameError: name 'str_7' is not defined

print("*" * 20 + "字符串的常用方法" + "*" * 20)
# 字符串的常用方法
STR_8 = "a123abc"
print(STR_8.capitalize())  # A123abc 首字母大写
print(STR_8.count("a"))  # 2
print(STR_8.find("a"))  # 0
print(STR_8.index("a"))  # 0
print(
    STR_8.isalnum()
)  # True 如果字符串中的所有字符都是字母数字并且 字符串中至少有一个字符。
print(STR_8.islower())  # False
print(STR_8.isupper())  # False

print("   aa  ".strip())  # aa

print("**".join("abc"))

print("*" * 20 + "字符串遍历" + "*" * 20)
STR_9 = "123abc"
for i in STR_9:
    print(i, end=" -*- ")
print()
# for i in range(len(STR_9)):
#     print(STR_9[i], end=" -*- ")
for i,j in enumerate(STR_9):
    print(i,j, end=" -*- ")
print()

for i in enumerate(STR_9):
    print(i, type(i))
