import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots() 
cicloid, = plt.plot([], [], 'o', color='r')

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
  cicloid.set_data(update(R=1, t=i))

ani = FuncAnimation(fig, animate, frames=t, interval=10)

ani.save('anima_task1.gif')