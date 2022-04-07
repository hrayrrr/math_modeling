import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots() 
cicloid, = plt.plot([], [], 'o', color='r')
cicloid_line, = plt.plot([], [], '-', color='r')

xdata, ydata = [], []

def update(R, t):
  x = R * (t - (np.sin(t)))
  y = R * (1-((np.cos(t))))
  return x, y

edge = 50
plt.axis('equal')
ax.set_xlim(-edge, edge)
ax.set_ylim(-edge, edge)

def animate(i):
  cicloid.set_data(update(R=2, t=i))
  xdata.append(update(R=2, t=i)[0])
  ydata.append(update(R=2, t=i)[1])
  cicloid_line.set_data(xdata[:i],ydata[:i])

ani = FuncAnimation(fig, animate, frames=120, interval=40)

ani.save('lab_7_task1.gif')