# 不可变与可变类型
# 不可变，数字，字符串，元组，bool
str1 = "hello"
# str1[0] = 'H' # 报错 TypeError: 'str' object does not support item assignment
print(str1)
"""
数字类型的不可变性指的是数字对象的值不可变，而不是指数字对象本身不可变。具体来说，
对于整数、浮点数等内置数字类型，一旦创建了一个数字对象，其值就不能被修改。
"""
# 可变 列表，字典，集合
