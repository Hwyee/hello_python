# 数据类型的转换
# 数字字符串转整型
num = "123"
print(type(num))
num = int(num)
print(type(num))
num = float(num)
print(type(num))
# float转int
num = 123.456
num = int(num)
print(type(num))
print(num)
# bool转int
b1, b2 = True, False
print(int(b1), int(b2))

# int 转 float
num = 123
num = float(num)
print(type(num))
print(num)  # 123.0
# bool转float
b1, b2 = True, False
print(float(b1), float(b2))  # 1.0 0.0
# 字符串转布尔
s1, s2 = "True", "False"
print(bool(s1), bool(s2))  # True True 字符串有内容就是真
print(bool(""))  # False
print(bool(" "))  # True

# 进制转换
s = "100"
print(int(s, 2))  # 100 就是 4的二进制，如果有小数则自动去除小数
