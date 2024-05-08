time = "2024年5月8日23:38:48"
print("time is", time)  # 默认空格是分隔符 time is 2024年5月8日23:38:48

# 修改分隔符
print("time is", time, sep="------")  # time is------2024年5月8日23:38:48
# 修改结束语句
print(
    "time is", time, sep="000", end="\nits end\n"
)  # time is0002024年5月8日23:38:48  its end

# 格式化打印
print("time is %s" % time)

a = 1
b = 2
c = 3
print("a=%d,b=%d,c=%d" % (a, b, c)) # 小括号不能省略

# 保留两位小数
print("%.2f" % 3.1415926)  # 3.14

# 保留两位，位数不够用0填充
print("%02d" % 1)  # 01
