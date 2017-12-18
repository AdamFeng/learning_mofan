import matplotlib.pyplot as plt 
import numpy as np 

n = 12
X = np.arange(n)
Y1 = (1-X/float(n)) * np.random.uniform(0.5, 1.0, n)
Y2 = (1-X/float(n)) * np.random.uniform(0.5, 1.0, n)

plt.bar(X, +Y1)
plt.bar(X, -Y2)

plt.xlim(-.5,n)
plt.ylim(-1.25, 1.25)
plt.xticks(())
plt.yticks(())

# facecolor主体颜色，edgecolor边框颜色
plt.bar(X, +Y1, facecolor='#9999ff', edgecolor='white')
plt.bar(X, -Y2, facecolor='#ff9999', edgecolor='white')

# plt.text在柱体上下加上数值 
# ha='center'：横向居中对齐
# va='bottom'：纵向底部（顶部）对齐
for x,y in zip(X,Y1):
    plt.text(x, y+0.05, '%.2f'%y, ha='center', va='bottom')

for x,y in zip(X, Y2):
    plt.text(x, -y-0.05, '%.2f'%y, ha='center', va='top')

plt.show()