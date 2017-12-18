# numpy 索引

import numpy as np 
A = np.arange(3,15).reshape(3,4)
print(A)
print(A[2][1])  # ==A[2,1]
print(A[2,:])   # 第2行所有数
print(A[:,1])   # 第1列所有数

# 打印每一行
for row in A:
    print(row)

# 打印每一列
for column in A.T:
    print(column)

print(A.flatten()) # 把矩阵变成单行
#打印矩阵中每个元素
for item in A.flat:
    print(item)