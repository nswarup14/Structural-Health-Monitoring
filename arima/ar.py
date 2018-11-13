from statsmodels.tsa.arima_model import AR
from pandas import read_csv
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def main():
	series = read_csv('/home/akshit/Documents/Downloads/2.csv', header=0, index_col=0, squeeze=True)
	series.columns = ['a', 'b', 'c', 'd']
	series['e'] = pow((series['a']*series['a'] + series['b']*series['b'] + series['c']*series['c']), 0.5)

	df = pd.DataFrame({'$a': series['e']})


	fd = np.array(df)
	plt.plot(fd)



	model = AR(fd)
	results = model.fit()
	r = results.predict()
	plt.plot(r)
	plt.xlabel("Indices",fontsize=12)
	plt.ylabel("Data",fontsize=12)
	plt.show()
