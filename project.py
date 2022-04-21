import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

fig = plt.figure()
ax = plt.subplot()
ax.axis('equal')

t = np.linspace(0, 30*np.pi, 400)

R = 37
r = 15

x = ((R - r) * np.cos(t)) + (r * np.cos(t * ((R - r)/r)))
y = ((R - r) * np.sin(t)) - (r * np.sin(t * ((R - r)/r)))

f = np.linspace(0, 10*np.pi, 100)

lcircle_x = R*np.cos(f)
lcircle_y = R*np.sin(f)
ax.plot(lcircle_x, lcircle_y, 'black', lw=1)

scircle_x = r*np.cos(f)
scircle_y = r*np.sin(f)

dx = (R-r)*np.cos(t)
dy = (R-r)*np.sin(t)

hypocycloids = []
circles = []
points = []

def animate(i):
  if len(circles) > 0:
    circles.pop().remove()
    hypocycloids.pop().remove()
    points.pop().remove()

  circle, = ax.plot(dx[i]+scircle_x, dy[i]+scircle_y, 'black',lw=0.5)
  hypocycloid, = ax.plot(x[:i+1], y[:i+1], 'blue', lw=2)
  point, = ax.plot(x[i], y[i], 'ro', markersize=10)

  circles.append(circle)
  hypocycloids.append(hypocycloid)
  points.append(point)

ani = FuncAnimation(fig, animate, frames=400, interval=50, repeat_delay=2000)
ani.save('hypocycloid.gif')