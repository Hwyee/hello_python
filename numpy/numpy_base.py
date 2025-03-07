import numpy

#支持大量的维度数组与矩阵运算，此外也针对数组运算提供大量的数学函数库。

#ndarray numpy.array(object, dtype = None, copy = True, order = None, subok = False, ndmin = 0)
# object->数组或数列 dtype->类型可选 copy->是否可复制可选  order ->创建数组的样式，C行方向，F列方向，A任意 subok->返回一个与基类类型一样的数组 ndmin->最小维度


# 最小维度  
import numpy as np 
a = np.array([1, 2, 3, 4, 5], ndmin =  2)  
print (a) #[[1 2 3 4 5]]

# dtype 参数  
import numpy as np 
a = np.array([1,  2,  3], dtype = complex)  
print (a) #[1.+0.j 2.+0.j 3.+0.j]