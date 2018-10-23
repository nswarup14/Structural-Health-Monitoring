import numpy as np
import matplotlib.pyplot as plt
from numpy.fft import fft,fftfreq, ifft

def DFT_slow(x):
    x = np.asarray(x, dtype=float)
    N = x.shape[0]
    n = np.arange(N)
    k = n.reshape((N, 1))
    M = np.exp(-2j * np.pi * k * n / N)
    return np.dot(M, x)


def FFT(x):
    #recursive cooley fft
    x = np.asarray(x, dtype=float)
    N = x.shape[0]
    
    if N % 2 > 0:
        raise ValueError("size of x must be a power of 2")
    elif N <= 5:
        return DFT_slow(x)
    else:
        X_even = FFT(x[::2])
        X_odd = FFT(x[1::2])
        
        factor = np.exp(-2j * np.pi * np.arange(N) / N)
        
        print(X_even + factor[:int(N / 2)] * X_odd)
        return np.concatenate([X_even + factor[:int(N / 2)] * X_odd,
                               X_even + factor[int(N / 2):] * X_odd])


#setup domain
#number of points
n = 8

#time length in secs
l = 1


#creating signals
t=np.linspace(0,l,n)
x1=[1,10,2,9,5,6,7,8]

y1=FFT(x1)

freq=fftfreq(n)
mask=freq>0
y2=2*np.abs(y1/n)

#t,x1
#freq,y
#freq[mask],y2[mask]
