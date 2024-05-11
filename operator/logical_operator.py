# 逻辑运算符
# and  or  not 自带短路运算
a = 10
b = 20
print("a =", a, "b =", b)
if a > 0 and b > 0:
    print("两个数都大于0")
else:
    print("有一个数不大于0")

if a > 0 or b > 0:
    print("至少有一个数大于0")
else:
    print("两个数都不大于0")

if not a > 0:
    print("a不大于0")
else:
    print("a大于0")


# 短路运算
s1 = "hello"
s2 = "world"
print(s1 or s2)  # 输出s1 hello
print(s1 and s2)  # 输出s2 world

# 优先级 not>and>or
print(s1 or not s2)
