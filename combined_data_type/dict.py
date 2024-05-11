# 字典 无序 键是唯一的，key只能是字符串，数字，元组，值可以是任何类型

# 创建
dict1 = {"name": "zhangsan", "age": 18, "sex": "male", 1: 1, (1, 2): "tuple"}
print(dict1)
print(type(dict1))
dict2 = dict(name="zhangsan", age=18, sex="male")
print(dict2)
dict3 = dict([("name", "zhangsan"), ("age", 18), ("sex", "male")])
print(dict3)
# 如果键重复了，会覆盖之前的
dict4 = {"name": "zhangsan", "age": 18, "sex": "male", "name": "lisi"}
print(dict4)
# dict5 = dict(name="zhangsan", age=18, sex="male", name="lisi") # SyntaxError: keyword argument repeated: name
# print(dict5)

# 新增键值对
dict1["address"] = "beijing"
print(dict1)

# 获取键值对
print(dict1["age"])  # 18

# 修改键值对
dict1["age"] = 19
print(dict1)
dict1.update({"address": "beijing999"})
print(dict1)
# update也可以新增
dict1.update({"update": 20})
print(dict1)

# 删除键值对
del dict1["age"]
print(dict1)

# 查询key是否存在 in 不能判断value
print("name" in dict1)  # True

# 遍历
print("*" * 20, "遍历key", "*" * 20)
for key in dict1:  # 遍历key
    print(key)
print("*" * 20, "遍历value", "*" * 20)
for value in dict1.values():  # 遍历value
    print(value)
print("*" * 20, "遍历key和value", "*" * 20)
for key, value in dict1.items():  # 遍历key和value
    print(key, value)
print("*" * 20, "遍历key和value (元组)", "*" * 20)
for item in dict1.items():  # 遍历key和value
    print(item)

# 字典的常用方法
dict1.pop("address")  # 删除键值对
print(dict1)
print(dict1.copy())  # 复制
dict1.popitem()  # 删除最后的键值对 pop出栈
print(dict1)
dict1.clear()  # 清空
print(dict1)
