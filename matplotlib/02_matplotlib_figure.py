import matplotlib.pyplot as plt
import numpy as np 

# 使用np.linspace定义x：范围是(-3,3);个数是50. 
# 仿真一维数据组(x ,y1)表示曲线1. 仿真一维数据组(x ,y2)表示曲线2.
x = np.linspace(-3,3,50)
y1 = 2*x + 1
y2 = x**2

# 设置figure的属性，每个plt.figure()之后的plt.plot()在一个figure中
plt.figure(num=3, figsize=(8,5))
plt.plot(x, y2)
plt.plot(x, y1, color='red', linewidth=1.0, linestyle='--')
plt.show()
