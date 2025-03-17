""" 数据类型的转换 """
# 数字字符串转整型
NUM = "123"
print(type(NUM))
NUM = int(NUM)
print(type(NUM))
NUM = float(NUM)
print(type(NUM))
# float转int
NUM = 123.456
NUM = int(NUM)
print(type(NUM))
print(NUM)
# bool转int
b1, b2 = True, False
print(int(b1), int(b2))

# int 转 float
NUM = 123
num = float(NUM)
print(type(NUM))
print(NUM)  # 123.0
# bool转float
b1, b2 = True, False
print(float(b1), float(b2))  # 1.0 0.0
# 字符串转布尔
s1, s2 = "True", "False"
print(bool(s1), bool(s2))  # True True 字符串有内容就是真
print(bool(""))  # False
print(bool(" "))  # True

# 进制转换
S = "100"
print(int(S, 2))  # 100 就是 4的二进制，如果有小数则自动去除小数
