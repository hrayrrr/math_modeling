import numpy as np

from physical_constants import g, k, e, h

h = 100
a = np.pi/3
b = 30

v = np.sqrt((g*h*(np.tan(b)**2))/(2*(np.cos(a)**2)*(1-np.tan(b)*np.tan(a))))
print(v)

T = 200
E = 300

N = (2/np.sqrt(np.pi)) * (h/((k*T)**(3/2))) * (e**(-E/(k*T))) * (E**(T/2))
print(N)