import numpy as np
import matplotlib.pyplot as plt
from numpy.fft import fft,fftfreq, ifft

def main(cf1,cf2,cf3,cf4,list_func,l,n):
	#setup domain
	#number of points
	coff_list=[]
	try:
		#print(cf1," ",cf2," ",cf3," ",cf4)
		#print("sadad")
		if(cf1==""):
			coff_list.append(0)
		else:
			coff_list.append(int(cf1))

		if(cf2==""):
			coff_list.append(0)
		else:
			coff_list.append(int(cf2))

		if(cf3==""):
			coff_list.append(0)
		else:
			coff_list.append(int(cf3))

		if(cf4==""):
			coff_list.append(0)
		else:
			coff_list.append(int(cf4))

		l=int(l)
		n=int(n)


	except ValueError as e:
		return
	#angular frequency
	#print("sadad")
	omg=2*np.pi/l

	#creating signals
	x=np.linspace(0,l,n);
	y1=y2=y3=y4=0
	y=0

#	for count in range(0,len(list_func)):
#		print(coff_list[count]," ",list_func[count])


	for each_item_index in range(0,len(list_func)):
		if(list_func[each_item_index]=="none"):
			pass
		else:
			if(list_func[each_item_index]=="sine"):
				print(list_func[each_item_index])
				y += 1*np.sin(int(coff_list[each_item_index])*omg*x)
			else:
				print(list_func[each_item_index])
				y += 1*np.cos(int(coff_list[each_item_index])*omg*x)



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

