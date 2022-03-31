import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots()
bab, = plt.plot([], [], 'o', color='r')

xdata, ydata = [], []

def ur(t):
  x = np.sin(t) * ((np.e**np.cos(t)) - 2 * (np.cos(4*t)) - ((np.sin(t / 12))**5))
  y = np.cos(t) * ((np.e**np.cos(t)) - 2 * (np.cos(4*t)) - ((np.sin(t / 12))**5))
  return x, y
edge = 10
plt.axis('equal')
ax.set_xlim(-edge, edge)
ax.set_ylim(-edge, edge)

coordsx = []
coordsy = []
t = np.linspace(0, 12*np.pi, 500)
for i in range(len(t)):
  coordsx.append(ur(t=t[i])[0])
  coordsy.append(ur(t=t[i])[1])

def update(i):
  bab.set_data(coordsx[:i], coordsy[:i])
  

ani = FuncAnimation(fig, update, frames=len(coordsx), interval=40)

ani.save('anima_task3.gif')