import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots()
frac, = plt.plot([], [], 'o', color='r')

xdata, ydata = [], []

x0 = 0.1
y0 = 0.1
C = 0.3
D = 0.33

def fractal(x0, y0, C, D):
  