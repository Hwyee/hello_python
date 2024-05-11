# 位运算符
a = 0b101
b = 0b011
print(a & b)  # 0b001
print(a | b)  # 0b111
print(a ^ b)  # 0b110
print(~a)  #  -6
print(~a + 1)  # -5 取反+1就是相反数
print(a << 2)  # 0b101 << 2 = 0b10100  左移两位
print(a >> 2)  # 0b101 >> 2 = 0b1 右移两位
print(a & 0b1111)  # 0b101 & 0b1111 = 0b101 和掩码进行与操作，还是本身
print(a | 0b1111)  # 0b101 | 0b1111 = 0b1111 和掩码进行或操作，结果是掩码

a = -0b101
print(a)
