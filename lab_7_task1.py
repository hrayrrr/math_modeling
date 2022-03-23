import matplotlib.pyplot as plt
import numpy as np

def cycloid(r):
  x = []
  y = []
  for i in np.linspace(-2*np.pi, 2*np.pi, 100):
    x.append(r*(i - np.sin(i)))
    y.append(r*(1 - np.cos(i)))
  plt.plot(x,y)
  plt.show()

cycloid(5)

def astroida():
  x=[]
  y=[]
  for i in range (1,1000):
    x.append((np.sin(i))**3)
    y.append((np.cos(i))**3)
  plt.plot(x,y)
  plt.show()

astroida()