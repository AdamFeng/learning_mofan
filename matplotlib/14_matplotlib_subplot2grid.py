import matplotlib.pyplot as plt 
import matplotlib.gridspec as gridspec
import numpy as np 

plt.figure()

# 使用subplot2grid画图
# 分为3行3列，从0行0列开始plot，跨越3列1行
'''
ax1 = plt.subplot2grid((3,3),(0,0), colspan=3, rowspan=1)
ax1.plot([1,2],[1,2])
ax1.set_title('ax1_title')

ax2 = plt.subplot2grid((3,3),(1,0), colspan=2)
ax3 = plt.subplot2grid((3,3),(1,2), rowspan=2)
ax4 = plt.subplot2grid((3,3),(2,0))
ax5 = plt.subplot2grid((3,3),(2,1))

ax4.scatter([1,2],[2,2])
ax4.set_xlabel('ax4_x')
ax4.set_ylabel('ax4_y')
'''

# 使用matplotlib.gridspec将图分为3行3列
'''
gs = gridspec.GridSpec(3,3)
ax1 = plt.subplot(gs[0,:])
ax2 = plt.subplot(gs[1,:2])
ax3 = plt.subplot(gs[1:,2])
ax4 = plt.subplot(gs[-1,0])
ax5 = plt.subplot(gs[-1,-2])
'''

# 使用subplots画小图，((ax11,ax12),(ax21,ax22))依次为4个小图
f,((ax11,ax12),(ax21,ax22)) = plt.subplots(2,2,sharex=True, sharey=True,)
ax11.scatter([1,2],[1,2])


# 紧凑显示图像
plt.tight_layout()
plt.show()