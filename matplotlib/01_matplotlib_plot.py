import matplotlib.pyplot as plt
import numpy as np 

# [-1,1]平分50段，生成50个点
x = np.linspace(-1,1,50)
y=x**2+1

plt.figure()
plt.plot(x, y)
plt.show()
