# numpy的基础运算

import numpy as np 

a = np.array([10,20,30,40])
b = np.arange(4)

print(a,b)
c = a - b # 逐个相加减，乘除

c = b**a # **是乘方

c = 10*np.sin(a) # sin,cos,tan都在numpy中有相应的函数

print(c)
print(b)
print(b==3)  # 输出True or False

# 矩阵乘法
a = np.array([[1,1], [0,1]]) # 定义矩阵--完全写出
b = np.arange(4).reshape((2,2)) # 定义2行2列矩阵--reshape

print(a)
print(b)

c = a*b # 对应位置相乘
c_dot = np.dot(a,b) # 矩阵乘法
c_dot_2 = a.dot(b) # 与上一行相同
print(c)
print(c_dot)
print(c_dot_2)

a = np.random.random((2,4)) # 随机创建2行4列的矩阵


print(a)
print(np.sum(a))  # 矩阵中所有元素求和
print(np.min(a))  # 矩阵中所有元素最小值
print(np.max(a))  # 矩阵中所有元素最大值

print(np.sum(a, axis=1))  # 矩阵中每行元素求和   axis=1指的是行
print(np.sum(a, axis=0))  # 矩阵中每列元素求和   axis=0指的是列
print(np.min(a, axis=0))  # 矩阵中每列元素最小值
print(np.max(a, axis=1))  # 矩阵中每行元素最大值


A = np.arange(12,0,-1).reshape((3,4))

print(A)
print(np.argmin(A)) # 矩阵中最小值的索引
print(np.argmax(A)) # 矩阵中最大值的索引
print(np.mean(A))   # 矩阵的平均值 == A.mean() ==np.average(A) 
print(np.median(A)) # 矩阵的中位数
print(np.cumsum(A)) # 逐个元素累加值
print(np.diff(A))   # 相邻元素间的差（矩阵形式）
print(np.nonzero(A))# 每个非0元素索引
print(np.sort(A))   # 逐行排序
print(np.transpose(A)) # 矩阵转置 ==print(A.T)
print(np.clip(A, 5, 9)) # A中<5的数赋值为5，>9的数赋值为9
