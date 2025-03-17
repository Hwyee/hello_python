""" input() 相当于 scanf() Scanner,但是自带提示功能。"""
name = input("请输入你的名字：")
# print("你好，%s" % name)
print(f"你好{name}" )

#input()接收的数据都是<class 'str'>类型，所以要转换成其他类型，需要使用int()、float()等函数。
num = input("请输入一个数字：")
print(type(num))
num = int(num)
print(num + 1)
