import numpy as np
import pywt
import matplotlib.pyplot as plt
import csv
import sys
import math
from pandas import read_csv
import pandas as pd
def main(file_name):
	d=0; #take d also as input
	#load a data y
	y = []


	"""
	with open(file_name,'r+') as f:
	    reader = csv.reader(f,delimiter = ' ', quotechar='|')
	    for number in reader:
	       y.append(number[d])
	ts=y
	(ca, cd) = pywt.dwt(ts,'haar')
	"""
	
	
	series = read_csv(file_name, header=0, index_col=0, squeeze=True)
	series.columns = ['a', 'b', 'c', 'd']
	series['e'] = pow((series['a']*series['a'] + series['b']*series['b'] + series['c']*series['c']), 0.5)

	df1 = pd.DataFrame({'$a': series['e']})
	df= df1.iloc[:,0]
	#print(df)
	(ca, cd) = pywt.dwt(df,'haar')

	cat = pywt.threshold(ca, np.std(ca)/2, 'soft')
	cdt = pywt.threshold(cd, np.std(cd)/2, 'soft')

	
	ts_rec = pywt.idwt(cat, cdt, 'haar')


	plt.close('all')

	plt.subplot(211)
	# Original coefficients
	plt.plot(ca, '--*b')
	plt.plot(cd, '--*r')
	# Thresholded coefficients
	plt.plot(cat, '--*c')
	plt.plot(cdt, '--*m')
	plt.legend(['ca','cd','ca_thresh', 'cd_thresh'], loc=0)
	plt.grid(True)

	plt.subplot(212)
	

	#plt.plot(ts)
	
	plt.plot(df)
	#plt.hold('on')
	plt.plot(ts_rec, 'r')
	plt.legend(['original signal', 'reconstructed signal'])
	plt.grid(True)
	plt.show()


if __name__=='__main__':
	main()