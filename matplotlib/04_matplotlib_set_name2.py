import matplotlib.pyplot as plt 
import numpy as np 

x = np.linspace(-3,3,50)
y1 = 2*x+1
y2 = x**2

plt.figure()
plt.plot(x, y2)
plt.plot(x, y1, color='red', linewidth=1.0, linestyle='--')
plt.xlim((-1,2))
plt.ylim((-2,3))

new_ticks = np.linspace(-1,2,5)
plt.xticks(new_ticks)
plt.yticks([-2, -1.8, -1, 1.22, 3],['$really\ bad$', '$bad$', '$normal$', '$good$', '$really\ good$'])

# gca = get current axis:获取当前坐标轴信息
# 设置边框为none,不显示top和right的边框
ax = plt.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')

# 使用边框bottom代替x坐标轴
ax.xaxis.set_ticks_position('bottom')
# 使用边框left代替y坐标轴
ax.yaxis.set_ticks_position('left')

# set_position （位置所有属性：outward，axes，data）
# 设置边框bottom,left的位置
ax.spines['bottom'].set_position(('data',0))
ax.spines['left'].set_position(('data',0))
plt.show()