""" 时间库 """
import time

# 时间戳
print(time.time())
# 获取当前时间
print(time.localtime())  # 本地时间
print(time.gmtime())  # greenwich时间
# 字符串化时间
print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
print(time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime()))
print(time.strftime("%y-%m-%d %H:%M:%S", time.localtime(time.time())))
