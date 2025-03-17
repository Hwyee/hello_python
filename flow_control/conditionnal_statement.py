""" 条件语句 一定要有缩进！！！"""
T = True
F = False
if T:
    print("True")
elif F:
    print("False")
else:
    print("else")
print("end")

# 语句嵌套
if T:
    if F:
        print("False")
    else:
        print("else")
else:
    print("else")

# match语句，python3.10新特性， 和switch-case语句不同，没有break,其实和if-elif-else语句类似，但是更简洁
match 1:
    case 1:
        print("1")
    case 2:
        print("2")
    case _:
        print("_")

# match 元组
match (1, 2):
    case (1, 2, 3):
        print("1,2")
    case (1, _):
        print("1,_")
    case (_, 2):
        print("_,2")
    case _:
        print("_")
