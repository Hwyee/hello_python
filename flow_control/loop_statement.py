"""循环语句"""

print("循环语句\n" * 5)
print(len("\n"))
i = 0

# 1. while 循环
while i < 5:
    print("while 循环", i)
    i += 1
print("while 循环结束")

# 1.1 while 循环的 else 语句
i = 3
while i < 5:
    print("while else 循环", i)
    i += 1
else:
    print("while  else 循环结束")
# 如果循环 break 跳出，则 else 语句块中的代码不会执行
i = 3
while i < 5:
    print("while else break 循环", i)
    break
    i += 1
else:
    print("while  else break 循环结束")

# 2. for 循环
for i in range(5):
    print("for 循环", i)
print("for 循环结束")

# 3. break 跳出循环
for i in range(5):
    if i == 3:
        break
    print("break 跳出循环", i)
print("break 跳出循环结束")

# 4. continue 跳过当前循环
for i in range(5):
    if i == 3:
        continue
    print("continue 跳过当前循环", i)
print("continue 跳过当前循环结束")

# 5. pass 占位符


# pass 是 Python 中的一个关键字，它在代码中起着占位符的作用，表示不执行任何操作。
# 当你需要一个语句块，但暂时不想或不需要放入任何实际代码时
# python的代码块必须要有语句,就可以使用pass占位,这样就不会报错。

for i in range(5):
    pass

print("pass 占位符结束")

if i == 3:
    pass
else:
    pass


# 6. 嵌套循环
for i in range(5):
    for j in range(5):
        print("嵌套循环", i, j)
print("嵌套循环结束")

# 7. 循环语句的嵌套
for i in range(5):
    for j in range(5):
        if i == 3:
            break
        print("循环语句的嵌套", i, j)
print("循环语句的嵌套结束")


# python 没有类似label的语句

# 九九乘法表
for i in range(1, 10):
    for j in range(1, i + 1):
        # print("%d * %d = %d" % (i, j, i * j), end="\t")
        print(f"{i}*{j}={i * j}", end="\t")
    print()
