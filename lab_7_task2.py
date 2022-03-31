import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots()
krug, = plt.plot([], [], 'o', color='r')

xdata, ydata = [], []

def circle_move(R):
  alpha = np.arange(0, 2*np.pi, 0.1)
  x = R * np.cos(alpha)
  y = R * np.sin(alpha)
  return x, y

edge = 3
plt.axis('equal')
ax.set_xlim(-edge, edge)
ax.set_ylim(-edge, edge)

t = np.arange(0, 2*np.pi, 0.1)

def update(i):
  krug.set_data(circle_move(R=0.05*i))

ani = FuncAnimation(fig, update, frames=120, interval=50)

ani.save('lab_7_task2.gif')