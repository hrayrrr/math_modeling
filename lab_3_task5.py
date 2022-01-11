import numpy as np

N = 3
M = 4

nxm = []

for i in range(N):
  a = []
  for j in range(M):
    a.append(np.sin(N*(i+1) + M*(j+1)))
  nxm.append(a)

for i in range(N):
  nxm[i][0], nxm[i][1] = nxm[i][1], nxm[i][0]
  for j in range(M):
    if nxm[i][j] < 0:
      nxm[i][j] = 0
      print("%7.0f" % nxm[i][j], end='')
    else:
      print("%7.2f" % nxm[i][j], end='')
  print()