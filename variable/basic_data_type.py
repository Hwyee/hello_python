""" 整数"""
NUM1 = 1
print(NUM1)
NEGATIVE_NUM = -1
print(NEGATIVE_NUM)

# 浮点型
FLOAT_1 = 1.1
print(FLOAT_1)
float_2 = round(1.1, 2)
print(float_2)  # 1.1

# 复数
COMPLEX_1 = 1j
print(COMPLEX_1)

# 布尔类型
BOOL_1 = True
print(BOOL_1)


# 小整数缓存池
"""
Python的小整数池范围是固定的,包括从-5到256的所有整数。
这个池子的设计目的是为了提高性能,因为这些小整数在编程中非常常见,通过重用已经分配的内存,
可以避免频繁的内存分配和释放操作。在这个范围内的整数对象在Python解释器启动时就会被预先创建,
并且在整个解释器生命周期内都不会被垃圾回收。

需要注意的是,这个特性是Python标准解释器的行为,
对于不同的Python实现(如CPython),这个特性可能会有所不同。
例如,PyPy等其他Python实现可能有不同的优化策略。
此外,像PyCharm这样的集成开发环境(IDE)可能会有自己的优化,可能会扩展这个范围,
但这通常不是Python标准行为的一部分,而是IDE为了提升交互体验所做的额外工作。
对于这些IDE扩展的具体范围,没有统一的标准,可能会因版本或配置而异,一般不需要开发者直接关注。"""
NUM_1 = 100
NUM_2 = 100
print(NUM_1 is NUM_2)  # True
print(id(NUM_1),"==",id(NUM_2))
