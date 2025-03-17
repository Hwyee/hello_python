"""  逻辑运算符 """
# And  or  not 自带短路运算
A = 10
B = 20
print("A =", A, "B =", B)
if A > 0 and B > 0:
    print("两个数都大于0")
else:
    print("有一个数不大于0")

if A > 0 or B > 0:
    print("至少有一个数大于0")
else:
    print("两个数都不大于0")

if not A > 0:
    print("A不大于0")
else:
    print("A大于0")


# 短路运算
S1 = "hello"
S2 = "world"
print(S1 or S2)  # 输出s1 hello
print(S1 and S2)  # 输出s2 world

# 优先级 not>And>or
print(S1 or not S2)
