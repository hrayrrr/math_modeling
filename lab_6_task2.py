import matplotlib.pyplot as plt
import numpy as np

def parabola_giperbola(x1=-10, x2=10, x3=0.01, x4=10, N=0.01, a=1, b=1, c=0, k=1, label='parabola & giperbola'):
  xp = np.arange(x1, x2, N)
  xg = np.arange(x3, x4, N)
  y1 = a*xp**2 + b*xp + c
  y2 = k/xg
  plt.plot(xp, y1)
  plt.plot(xg, y2)
  plt.show()

parabola_giperbola()