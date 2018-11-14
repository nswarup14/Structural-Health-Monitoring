from statsmodels.tsa.arima_model import AR
from pandas import read_csv
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

def main():
	filepath=os.path.abspath(os.curdir) 
	series = read_csv(filepath+"/2.csv", header=0, index_col=0, squeeze=True)
	series.columns = ['a', 'b', 'c', 'd']
	series['e'] = pow((series['a']*series['a'] + series['b']*series['b'] + series['c']*series['c']), 0.5)

	df = pd.DataFrame({'$a': series['e']})
	print(df)

	fd = np.array(df)
	plt.plot(fd)



	model = AR(fd)
	results = model.fit()
	r = results.predict()
	plt.plot(r)
	plt.xlabel("Indices",fontsize=12)
	plt.ylabel("Data",fontsize=12)
	plt.show()

if __name__ == '__main__':
	main()