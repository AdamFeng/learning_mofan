import numpy as np 

A = np.arange(12).reshape((3,4))
print(A)
'''
[[ 0  1  2  3]
 [ 4  5  6  7]
 [ 8  9 10 11]]
 '''

print(np.split(A, 2, axis=1)) # 对A进行分割，按列
print(np.split(A, 3, axis=0)) # 对A进行分割，按行

# np.split不能进行不等分割，np.array_split可以进行不等分割
print(np.array_split(A,2,axis=0))

print(np.vsplit(A,3)) # 纵向分割，按行
print(np.hsplit(A,2)) # 横向分割，按列