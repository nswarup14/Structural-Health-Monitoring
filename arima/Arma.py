from statsmodels.tsa.arima_model import ARMA
from pandas import read_csv
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def main(p,q):
	#print("Armaasdasddasd")
	series = read_csv('/home/akshit/Documents/Downloads/2.csv', header=0, index_col=0, squeeze=True)
	series.columns = ['a', 'b', 'c', 'd']
	series['e'] = pow((series['a']*series['a'] + series['b']*series['b'] + series['c']*series['c']), 0.5)

	df = pd.DataFrame({'$a': series['e']})


	fd = np.array(df)
	plt.plot(fd)

	p = int(p)
	q = int(q)

	model = ARMA(fd, order=(p, q))


	results = model.fit()

	r = results.predict()

	#print("ResultsARMA")
	plt.plot(r)
	plt.show()