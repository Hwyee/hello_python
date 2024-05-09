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
