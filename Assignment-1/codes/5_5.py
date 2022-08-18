import numpy as np
import matplotlib.pyplot as plt

x = np.loadtxt("x(n).dat")
toeplitz = np.loadtxt("toeplitz.dat")
k=25
y = np.dot(toeplitz, x)

plt.stem(range(0,k),y)
plt.xlabel('$n$')
plt.ylabel('$y(n)$')
plt.grid()
plt.show()