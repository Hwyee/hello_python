# 集合 没有重复元素，无序
set1 = {1, 2, 3, 4, 5, 5}
print(set1)  # {1, 2, 3, 4, 5}
# 空集合
set2 = set()
print(set2)  # set()
print(type(set2))  # <class 'set'>
# 空集合不能用{}表示
set3 = {}
print(type(set3))  # <class 'dict'>

# list->set
list1 = [1, 2, 3, 4, 5, 5]
set1 = set(list1)
print(set1)  # {1, 2, 3, 4, 5}
# set->list
set1 = {1, 2, 3, 4, 5, 5}
list1 = list(set1)
print(list1)
# set->tuple
set1 = {1, 2, 3, 4, 5, 5}
tuple1 = tuple(set1)
print(tuple1)
# set->str
set1 = {1, 2, 3, 4, 5, 5}
str1 = str(set1)
print(str1)  # {1, 2, 3, 4, 5}

# dict->set
dict1 = {"name": "张三", "age": 18, "sex": "男"}
set1 = set(dict1)
print(set1)  # {'sex', 'age', 'name'}


# 通用函数
set4 = {1, 2, 3, 4, 5, 5}
print(len(set4))
print(max(set4))
print(min(set4))
print(sum(set4))
print(sorted(set4))
print(1 in set4)

# 集合不可以使用索引
# print(set4[0]) # TypeError: 'set' object is not subscriptable

# 集合遍历
print("*" * 20, "集合遍历")
for i in set4:
    print(i)

# 常用方法
set5 = {1, 2, 3, 4, 5, 5}
set5.add(6)
print(set5)
set5.remove(6)
print(set5)
set5.clear()
print(set5)
set5.update([1, 2, 3, 4, 5, 5])  # 并集合并
print(set5)

# 交集 并集
print("交集并集")
set6 = {1, 2, 3, 4, 5, 5}
set7 = {1, 2, 3, 4, 5, 5, 6, 7}
print(set6 & set7)
print(set6 | set7)
