import matplotlib.pyplot as plt 
import numpy as np 

n = 1024 
X = np.random.normal(0,1,n) # 每一个点X值
Y = np.random.normal(0,1,n) # 每一个点Y值
T = np.arctan2(Y,X) # 设置每个点颜色

plt.scatter(X, Y, s=75, c=T, alpha=.5)

plt.xlim(-1.5,1.5)
plt.xticks(()) # 忽略ticks
plt.ylim(-1.5,1.5)
plt.yticks(()) # 忽略ticks

plt.show()