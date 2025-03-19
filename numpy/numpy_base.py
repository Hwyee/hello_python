"""
支持大量的维度数组与矩阵运算，此外也针对数组运算提供大量的数学函数库
"""

import numpy as np

# ndarray numpy.array(object, dtype = None, copy = True, order = None, subok = False, ndmin = 0)
# object->数组或数列 dtype->类型可选 copy->是否可复制可选
# order ->创建数组的样式，C行方向，F列方向，A任意 subok->返回一个与基类类型一样的数组 ndmin->最小维度


# 最小维度

a = np.array([1, 2, 3, 4, 5], ndmin=2)
print(a)  # [[1 2 3 4 5]]

# dtype 参数
b = np.array([1, 2, 3, 4 + 1j], dtype=complex)
print(b)  # [1.+0.j 2.+0.j 3.+0.j 4.+1.j]
print(1 + 1j, 1 + 0j)  # (1+1j) (1+0j)

# 轴 秩  空间概念属于说是这个那个我的你的 难受

print(a.ndim)  # 2

# 维度 是一个元组  就是数组的行列
print(a.shape)  # (1, 5)

# 调整数组的维度
a1 = np.array([[1, 2, 3], [4, 5, 6]])
b1 = a1.reshape(3, 2)
print(b1)

#  itemsize 获取数组中元素的大小
# 数组的 dtype 为 int8（一个字节）
x = np.array([1, 2, 3, 4, 5], dtype=np.int8)
print(x.itemsize)  # 1

# 数组的 dtype 现在为 float64（八个字节）
y = np.array([1, 2, 3, 4, 5], dtype=np.float64)
print(y.itemsize)  # 8

# 存放数据v的内存地址
print(x.data)  # <memory at 0x7f434b4fbf40>

# flags 获取数组的标志
#   C_CONTIGUOUS : True 表示数组是连续的
#   F_CONTIGUOUS : True 表示数组是按列连续的
#   OWNDATA : True 表示数组拥有自己的数据
#   WRITEABLE : True 表示数组可以修改
#   ALIGNED : True 表示数组的数据是按字节对齐的
#   WRITEBACKIFCOPY : False 表示数组不是通过视图修改的 视图创建相当于拷贝
#   UPDATEIFCOPY (已弃用): False 表示数组不是通过视图修改的 视图创建相当与拷贝
print(y.flags)
