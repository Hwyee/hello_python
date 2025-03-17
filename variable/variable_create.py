""" 相同变量连续赋值 """
A = B = C = 10
print("a =", A)  # a = 10

# 不同变量用元组连续赋值
d, e = 10, 20

A = 20
print("a =", A)  # a = 20

A = "hello"
print("a =", A)  # a = hello

CONST = 999
print("CONST =", CONST)

# 标识符,字母下划线,数字,不能以数字开头
HELLO_WORLD = "hello world"
NUM_1 = 1
