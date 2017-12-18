# 创建array

import numpy as np 
a = np.array([2, 23, 4], dtype = np.int64) # dtype设置数组中元素的类型
b = np.zeros((3,4)) # 定义3行4列全为0的矩阵
c = np.ones((3,4), dtype=np.int)
d = np.arange(12).reshape((3,4)) # 生成3行4列从0到11的矩阵
e = np.empty((3,4)) # 生成3行4列无限接近于0的矩阵

print(a.dtype)  # int64：array中元素的类型
print(b)        # [[ 0.  0.  0.  0.]
                #  [ 0.  0.  0.  0.]
                #  [ 0.  0.  0.  0.]]
print(c)        # [[1 1 1 1]
                #  [1 1 1 1]
                #  [1 1 1 1]]
print(d)        # [[ 0  1  2  3]
                #  [ 4  5  6  7]
                #  [ 8  9 10 11]]
print(e)        # [[  6.23042070e-307   1.89146896e-307   1.37961302e-306   1.05699242e-307]
                #  [  8.01097889e-307   1.78020169e-306   7.56601165e-307   1.02359984e-306]
                #  [  1.33510679e-306   2.22522597e-306   1.33511018e-306   2.31301135e-312]]