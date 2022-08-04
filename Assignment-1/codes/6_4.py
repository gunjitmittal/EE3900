import numpy as np
import matplotlib.pyplot as plt
#If using termux
# import subprocess
# import shlex
#end if


N = 14
n = np.arange(N)
fn=(-1/2)**n
hn1=np.pad(fn, (0,2), 'constant', constant_values=(0))
hn2=np.pad(fn, (2,0), 'constant', constant_values=(0))
h = hn1+hn2

xtemp=np.array([1.0,2.0,3.0,4.0,2.0,1.0])
x=np.pad(xtemp, (0,8), 'constant', constant_values=(0))

X = np.fft.fft(x)

H = np.fft.fft(h, N)

Y = X * H

y = np.fft.ifft(Y)

plt.stem(range(0,N),np.real(y))
plt.title('Filter Output using FFT and IFFT')
plt.xlabel('$n$')
plt.ylabel('$Y(n)$')
plt.grid()
#If using termux
plt.savefig('../figs/6_4.pdf')