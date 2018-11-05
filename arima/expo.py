from pandas import read_csv
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def main(alpha):
	alpha=float(alpha)
	series = read_csv('/home/akshit/Documents/Downloads/2.csv', header=0, index_col=0, squeeze=True)
	series.columns = ['a', 'b', 'c', 'd']
	series['e'] = pow((series['a']*series['a'] + series['b']*series['b'] + series['c']*series['c']), 0.5)

	df = pd.DataFrame({'$a': series['e']})


	fd = np.array(df)
	plt.plot(fd)

	#alpha = float(input())

	for x in range(0, len(fd)):
	    if(x>0 and x<len(fd)-1):
	        fd[x] = alpha*fd[x] + (1-alpha)*fd[x-1]

	plt.plot(fd)
	plt.show()

if __name__ == '__main__':
	main()