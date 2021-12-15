import numpy as np

from physical_constants import g

v0 = int(input('v0 = '))
x0 = int(input('x0 = '))
y0 = int(input('y0 = '))

t1 = 0
x1 = x0 + v0 * t1
y1 = y0 + v0 * t1 - ((g*(t1**2))/2)

t2 = 1
x2 = x0 + v0 * t2
y2 = y0 + v0 * t2 - ((g*(t2**2))/2)

t3 = 2
x3 = x0 + v0 * t3
y3 = y0 + v0 * t3 - ((g*(t3**2))/2)

t4 = 3
x4 = x0 + v0 * t4
y4 = y0 + v0 * t4 - ((g*(t4**2))/2)

t5 = 4
x5 = x0 + v0 * t5
y5 = y0 + v0 * t5 - ((g*(t5**2))/2)

t6 = 5
x6 = x0 + v0 * t6
y6 = y0 + v0 * t6 - ((g*(t6**2))/2)

txy = [[t1, x1, y1], [t2, x2, y2], [t3, x3, y3], [t4, x4, y4], [t5, x5, y5], [t6, x6, y6]]
ttxxyy = np.array(txy)
print(ttxxyy)