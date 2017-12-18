import numpy as np 

A = np.array([1,1,1])[:,np.newaxis]  # 在纵向上增加一个维度
B = np.array([2,2,2])[:,np.newaxis]  # 在纵向上增加一个维度

C = np.vstack((A,B)) # 上下合并 vertical stack
print(C)
'''
[[1 1 1]
 [2 2 2]]
'''
D = np.hstack((A,B)) # 左右合并 horizontal stack
print(D)
'''
[1 1 1 2 2 2]
'''
print(A.T.shape)
'''
(3,)
'''
print(B.T.shape)
'''
(3,)
'''
print(C.T.shape)
'''
(3, 2)
'''
print(D.T.shape)
'''
(6,)
'''
# 单行数组不能靠T来转置

print(A[np.newaxis,:]) # np.newaxis增加一个维度，然后可以转置
print(A[:,np.newaxis]) # np.newaxis增加一个维度

C = np.concatenate((A,B,B,A), axis=1)  # np.concatenage进行多个array的合并
                                       # axis=0纵向合并  axis=1横向合并
print(C)