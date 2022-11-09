import matplotlib.pyplot as plt
import numpy as np
import scipy
import subprocess
import shlex

def xt(t,A0,f0):
    return A0*abs(np.sin(2*np.pi*f0*t))
vec_xt = scipy.vectorize(xt)

T = np.linspace(0,4/50,1000)

plt.plot(T,vec_xt(T,12,50))
plt.grid()
plt.xlabel('t')
plt.ylabel('x(t)')
plt.savefig('../figs/1_1.png')
plt.show()