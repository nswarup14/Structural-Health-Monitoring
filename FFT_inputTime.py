import numpy as np
import matplotlib.pyplot as plt
from numpy.fft import fft,fftfreq, ifft
import csv
import math


def main(sensor, file_name, l, m):
	#load a data y
	
	y = []
	
	with open(file_name,'r+') as f:
	    reader = csv.reader(f,delimiter = ' ', quotechar='|')
	    for number in reader:
	       y.append(number[0])



	#defining charachteristics of y
	y = np.asarray(y, dtype=float)
	n=y.shape[0]



	#l is total time of measurement, take input
	
	l=float(l)
	#print("Enter the sampling rate for which FFT is to be done")
	m=float(m)





	#FFT
	x=np.linspace(0,l,n);
	freq=fftfreq(n)
	mask=freq>0
	y1=fft(y)
	y2=2*np.abs(y1/n)



	#Graph
	Label = 'Original- '+sensor+' data'
	plt.figure(1)
	plt.title('Original Image')
	plt.plot(x,y,color='xkcd:salmon',label=Label)
	plt.legend()

	plt.figure(2)
	plt.title('FFT')
	plt.plot(freq[mask],y2[mask],label='true fft values')
	plt.show()
