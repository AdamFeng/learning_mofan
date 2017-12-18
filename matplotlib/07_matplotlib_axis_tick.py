import matplotlib.pyplot as plt 
import numpy as np 

x = np.linspace(-3,3,50)
y = 0.1*x 

plt.figure()

# 生成图片，设置zorder给plot在z轴方向排序
plt.plot(x,y, linewidth=10, zorder=1, color='darkblue')
plt.ylim(-2,2)
ax = plt.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data',0))
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data',0))

# 调整坐标
# 对遮挡的图像调节透明度
for label in ax.get_xticklabels() + ax.get_yticklabels():
    label.set_fontsize(12)
    # 设置label背景色，alpha设置透明度
    label.set_bbox(dict(facecolor='white', 
                        edgecolor='None', 
                        alpha=0.7, zorder=2))


plt.show()