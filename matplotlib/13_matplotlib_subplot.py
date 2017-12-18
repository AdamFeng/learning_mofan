# subplot:组合许多的小图, 放在一张大图里面显示的

import matplotlib.pyplot as plt 
import numpy as np 

plt.figure()

# 把整个figure均分成2行2列，
# 在第一个位置plot
# plt.subplot(2,2,1)
# plt.plot([0,1],[0,1])

# plt.subplot(2,2,2)
# plt.plot([0,1],[0,2])

# plt.subplot(2,2,3)
# plt.plot([0,1],[0,3])

# plt.subplot(224)
# plt.plot([0,1],[0,4])

# 画不均匀图中图
# 2行1列第一个位置
plt.subplot(211)
plt.plot([0,1],[0,1])

# 2行3列第4个位置，即下边第一个位置
plt.subplot(234)
plt.plot([0,1],[0,2])

plt.subplot(235)
plt.plot([0,1],[0,3])

plt.subplot(236)
plt.plot([0,1],[0,4])


plt.show()