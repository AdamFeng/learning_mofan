# numpy中array的属性

import numpy as np 

# 定义3行2列数组（列表转换为数组）
array = np.array([[1, 2, 3],
                  [2, 3, 4]])

print(array)
print('number of dim:', array.ndim) #几维数组 2
print('shape :',array.shape) # 几行几列 (2,3)
print('size:', array.size) # 有几个元素 6
