""" 异常处理
"""
try:
    print(1 / 0)
    print(1 + "1")
except ZeroDivisionError as e:  # as e表示将异常信息赋值给e
    print(e)
    print(ZeroDivisionError)
    print("除数不能为0")
except TypeError as e:
    print(e)
    print("类型不匹配")
except Exception as e:
    print(e)
    print("未知异常")
else:
    print("没有异常")
finally:
    print("无论是否异常都会执行")
