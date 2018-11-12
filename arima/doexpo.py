from pandas import read_csv
import pandas as pd
import numpy as np
#from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

def main(alpha,beta):
	series = read_csv('/home/akshit/Documents/Downloads/2.csv', header=0, index_col=0, squeeze=True)
	series.columns = ['a', 'b', 'c', 'd']
	series['e'] = pow((series['a']*series['a'] + series['b']*series['b'] + series['c']*series['c']), 0.5)

	df = pd.DataFrame({'$a': series['e']})


	fd = np.array(df)
	mn = fd
	plt.plot(fd)

	alpha = float(alpha)
	beta = float(beta)
	#random entry in an empty array
	#formula used from wikipedia
	b = [51]
	b.append(fd[1] - fd[0])

	for x in range(2, len(fd)-1):
    		mn[x]= alpha*fd[x] + (1-alpha)*(mn[x-1]-b[x-1])
    		b.append(beta*(mn[x] -mn[x-1]) + (1-beta)*(b[x-1]))

	plt.plot(mn)
	plt.xlabel('Data',fontsize=12)
	plt.ylabel('Indices',fontsize=12)
	plt.show()