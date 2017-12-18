import matplotlib.pyplot as plt 
import numpy as np 

x = np.linspace(-3,3,50)
y1 = 2*x + 1
y2 = x**2

plt.figure()
plt.plot(x, y2)
plt.plot(x, y1, color='red', linewidth=1.0, linestyle='--')

# 设置坐标轴的名字和范围
plt.xlim((-1,2))
plt.ylim((-2,3))
plt.xlabel(('I am x'))
plt.ylabel(('I am y'))

# 改变坐标轴上ticks的显示
# 使用plt.xticks设置x轴刻度：范围是(-1,2);个数是5.
# 使用plt.yticks设置y轴刻度以及名称：
# 刻度为[-2, -1.8, -1, 1.22, 3]；
# 对应刻度的名称为[‘really bad’,’bad’,’normal’,’good’, ‘really good’].
new_ticks = np.linspace(-1,2,5)
print(new_ticks)
plt.xticks(new_ticks)
plt.yticks([-2,-1.8,-1,1.22,3],[r'$really\ bad$', r'$bad$', r'$normal$', r'$good$', r'$really\ good$'])

plt.show()