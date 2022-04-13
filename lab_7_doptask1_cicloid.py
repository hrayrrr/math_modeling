import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

frames=300

def cicloid(R, t):
  x = R * (t- np.sin(t))
  y = R * (1 -np.cos(t))
  return x, y

def circle_func(R, N, t):
  x = np.zeros(N)
  y = np.zeros(N)
  for i in range(0, N, 1):
    alpha = np.linspace(0, 2*np.pi, N)
    x[i] = R * t + R * np.cos(alpha[i])
    y[i] = R + R * np.sin(alpha[i])
  return x, y

fig, ax = plt.subplots()
fig = plt.figure(figsize=(10,3), facecolor='pink', frameon=True)

ball, = plt.plot([], [], color='r')
ball2, = plt.plot([], [], 'o', color='g', ms=5)
ball3, = plt.plot([], [], color='b')

def animate(i):
  ball.set_data(cicloid(R=1, t=np.linspace(0, 4*np.pi*i/frames, i)))
  ball2.set_data(cicloid(R=1, t=4*np.pi*i/frames))
  ball3.set_data(circle_func(R=1, N=100, t=4*np.pi*i/frames))

ani = FuncAnimation(fig,
                   animate,
                   frames=frames,
                   interval=30)

plt.xlim(0,10)
plt.ylim(0,3)

ani.save('lab_7_doptask1_cicloid.gif')