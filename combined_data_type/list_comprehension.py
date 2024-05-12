# 列表推导式

l = [i for i in range(10)]
print(l)  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

sum(l)

g = (i for i in range(10))  # 生成器
print(g)  # <generator object <genexpr> at 0x0000022F4C03EB70>
for i in g:
    print(i)
print(list(g))


t = [(i, i + 1) for i in range(10) if i % 2 == 0]  # 元素为元组，需要加括号
print(t)

print([(1,), (2,)])

n = [[j for j in range(i)] for i in range(2, 10)]  # 嵌套列表推导式
print(n)


class A:
    pass


# 字典只要是有__hash__方法就可以当key，目前列表，
di = {(A(),): ""}
