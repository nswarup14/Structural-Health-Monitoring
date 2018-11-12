from statsmodels.tsa.arima_model import ARIMA
from pandas import read_csv
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

def main(p,d,q):
	#print("213323123123 starima")
	abspath= os.path.abspath(os.curdir)
	series = read_csv(abspath+'/2.csv', header=0, index_col=0, squeeze=True)
	series.columns = ['a', 'b', 'c', 'd']
	series['e'] = pow((series['a']*series['a'] + series['b']*series['b'] + series['c']*series['c']), 0.5)

	df = pd.DataFrame({'$a': series['e']})


	fd = np.array(df)
	plt.plot(fd)

	p = int(p)
	d = int(d)
	q = int(q)

	model = ARIMA(fd, order=(p, d, q))


	results = model.fit()

	r = results.predict()
	print("resultsARIMA")
	plt.plot(r)
	plt.xlabel('Data',fontsize=12)
	plt.ylabel('Indices',fontsize=12)
	plt.show()


