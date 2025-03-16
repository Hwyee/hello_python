"""打印"""

TIME = "2024年5月8日23:38:48"
print("time is", TIME)  # 默认空格是分隔符 time is 2024年5月8日23:38:48

# 修改分隔符
print("time is", TIME, sep="------")  # time is------2024年5月8日23:38:48
# 修改结束语句
print(
    "time is", TIME, sep="000", end="\nits end\n"
)  # time is0002024年5月8日23:38:48  its end

# 格式化打印
# print("time is %s" % TIME) # 旧方法
print(f"time is {TIME}")

A = 1
B = 2
C = 3
# print("a=%d,b=%.2f,c=%d" % (A, B, C))  # 小括号不能省略
print(f"a={A},b={B:.2f} c={C}") # a=1,b=2.00 c=3

# 保留两位小数
# print("%.2f" % 3.1415926)  # 3.14
print(f"{3.1415926:.2f}") # 3.14
# 保留两位，位数不够用0填充
# print("%02d" % 1)  # 01
print(f"{1:02d}") # 01
print(f"{1:2d}") # ' 1' 空格填充
# 不转义
print(r"反斜杠不转义\n\t\\")  # 反斜杠不转义\n\t\\
