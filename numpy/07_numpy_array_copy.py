import numpy as np 
a = np.arange(4)
print(a)

b = a
c = a
d = b

a[0] = 9

print(a)
print(b)
print(c)
print(d)

# = 的赋值方式会带有关联性，原值改变，全都改变
# copy() 的赋值方式没有关联性，改变间无联系

b = a.copy()
print(b)
a[2] = 22
print(b)
print(a)

