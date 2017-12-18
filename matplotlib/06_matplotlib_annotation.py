'''
当图线中某些特殊地方需要标注时，我们可以使用 annotation. 
matplotlib 中的 annotation 有两种方法，
 一种是用 plt 里面的 annotate，一种是直接用 plt 里面的 text 来写标注.
'''
import matplotlib.pyplot as plt 
import numpy as np 

x = np.linspace(-3,3,50)
y = 2*x + 1

plt.figure(num=1, figsize=(8,5),)
plt.plot(x,y)

# 移动坐标轴
ax = plt.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data',0))
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data',0))

# 标注点信息
x0 = 1
y0 = 2*x0 + 1
# 画虚线--(x0,0)和(x0,y0)之间，k：black，--：虚线
plt.plot([x0, x0,], [0, y0], 'k--', linewidth=2.5)
# 标注出(x0, y0)这个点
plt.scatter(x0, y0, s=50, color='b')

# 使用annotate对(x0, y0)点添加标注
# xycoords='data' 基于数据的值来选位置
# xytext=(+30, -30)和textcoords='offset points'：基于data的(+30,-30)位置来进行标注
# arrowprops设置箭头参数，arrowstyle设置箭头样式，connectionstyle设置弧度
plt.annotate(r'$2x+1=%s$' % y0, xy=(x0,y0), xycoords='data', 
            xytext=(+30, -30), textcoords='offset points', fontsize=16,
            arrowprops=dict(arrowstyle='->', connectionstyle='arc3, rad=.2')
            )

# 使用text添加注释
# (-3,7,3)是选取text的位置，fontdict设置文本字体
plt.text(-3.7, 3, r'$This\ is\ the\ some\ text.\ \mu\ \sigma_i\ \alpha_t$',
        fontdict={'size':16, 'color':'r'}
        )

plt.show()