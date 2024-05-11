# 文件操作
import os

print(os.getcwd())  # 执行路径
p = os.getcwd()
# 创建文件 rwa
f = open(p + "/test.txt", "w", encoding="utf-8")

f.write("hello world\n")
f.write("hello nil")
f.close()
#  读取文件 文件不存在抛出异常
# f = open("test1.txt", "r") # FileNotFoundError: [Errno 2] No such file or directory: 'test1.txt'
f = open(p + "/test.txt", "r")
print(f.read(5))
print(f.readline())
f.close()
f = open(p + "/test.txt", "r")
print(f.readlines())
f.close()

"""
文件mode：
r: 只读
w: 只写
a: 追加
r+: 读写
w+: 读写
a+: 读写
b: 二进制
t:文本 (默认)
+就是读写的意思

没有rw,ra这种写法
"""

# with语句 会自动关闭文件
with open(p + "/test.txt", "r") as f:  # 读
    print(f.read())
