import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

fig = plt.figure(facecolor='white')
ax = plt.subplot()

t = np.linspace(0, 30*np.pi, 400)

R = 37
r = 15

x = R * (np.cos(t)**3)
y = R * (np.sin(t)**3)

phi = np.linspace(0, 10*np.pi, 100)

lcircle_x = R*np.cos(phi)
lcircle_y = R*np.sin(phi)

ax.plot(lcircle_x, lcircle_y, 'black', lw=1)

scircle_x = r*np.cos(phi)
scircle_y = r*np.sin(phi)

dx = (R-r)*np.cos(t)
dy = (R-r)*np.sin(t)

astroids = []
circles = []
points = []

def animate(i):
  if len(circles) > 0:
    circles.pop().remove()
    astroids.pop().remove()
    points.pop().remove()
    
  circle, = ax.plot(dx[i]+scircle_x, dy[i]+scircle_y, 'black', lw=0.5)
  astroid, = ax.plot(x[:i+1], y[:i+1], 'blue', lw=2)
  point, = ax.plot(x[i], y[i], 'ro', markersize=10)
  
  circles.append(circle)
  astroids.append(astroid)
  points.append(point)
  
ax.axis('equal')

ani = FuncAnimation(fig, animate, frames=240, interval=40, repeat_delay=2000)

ani.save('lab_7_doptask1_astroid.gif')