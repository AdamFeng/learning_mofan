import matplotlib.pyplot as plt 
import matplotlib as mp
import numpy as np 

def f(x,y):
    return (1- x/2 + x**5 + y**3) * np.exp(-x**2-y**2)

n = 256
x = np.linspace(-3,3,n)
y = np.linspace(-3,3,n)

# 用meshgrid在二维平面中将每一个x和每一个y分别对应起来，编织成网格
X,Y = np.meshgrid(x,y)

# 使用plt.contourf进行颜色填充，从cmap中寻找f(X,y)对应的颜色，8代表将等高线分成10部分
plt.contourf(X, Y, f(X,Y), 8, alpha=.75, cmap=plt.cm.hot)

# 进行等高线绘制
C = plt.contour(X, Y, f(X,Y), 8, colors='black', linewidth=.5)

# 添加高度数字
plt.clabel(C, inline=True, fontsize=10)
plt.xticks(())
plt.yticks(())


plt.show()