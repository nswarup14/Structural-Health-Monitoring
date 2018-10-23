import numpy as np
import matplotlib.pyplot as plt
from numpy.fft import fft,fftfreq, ifft

def main():
	#setup domain
	#number of points
	n=int(input("Enter sampling rate: "))

	#time length in secs
	l= int(input("Enter time lenght in seconds, the time for which you want to perform the fft"))

	#angular frequency
	omg=2*np.pi/l

	#creating signals
	x=np.linspace(0,l,n);
	y1=1*np.cos(5*omg*x)
	y2=1*np.cos(10*omg*x)
	y3=0.5*np.cos(20*omg*x)

	y=y1+y2+y3

	freq=fftfreq(n)

	mask=freq>0

	fft_vals=fft(y)

	fft_theo=2*np.abs(fft_vals/n)

	plt.figure(1)
	plt.title('Original Image')
	plt.plot(x,y,color='xkcd:salmon',label='Original')
	plt.legend()

	plt.figure(2)
	plt.title('FFT')
	#plt.plot(freq,fft_vals,label='fft')
	#plt.title('True FFT')
	plt.plot(freq[mask],fft_theo[mask],label='true fft values')
	plt.show()


