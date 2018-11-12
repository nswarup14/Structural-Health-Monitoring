from statsmodels.tsa.holtwinters import ExponentialSmoothing, HoltWintersResults
from pandas import read_csv
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

def main(alpha,beta,gama):
	abspath= os.path.abspath(os.curdir)
	series = read_csv(abspath+'/2.csv', header=0, index_col=0, squeeze=True)
	series.columns = ['a', 'b', 'c', 'd']
	series['e'] = pow((series['a']*series['a'] + series['b']*series['b'] + series['c']*series['c']), 0.5)

	df = pd.DataFrame({'$a': series['e']})


	fd = np.array(df)
	plt.plot(fd)


	model = ExponentialSmoothing(fd)
	alpha = float(alpha)
	beta =  float(beta)
	gama = float(gama)

	a = ExponentialSmoothing.fit(model, smoothing_level=alpha, smoothing_slope=beta, use_boxcox=True,remove_bias=True, smoothing_seasonal=gama)
	c = HoltWintersResults.predict(a, start=0)
	plt.plot(c)
	plt.xlabel('Data',fontsize=12)
	plt.ylabel('Indices',fontsize=12)
	plt.show()
