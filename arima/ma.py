import matplotlib.pyplot as plt
from pandas import read_csv
import pandas as pd
import numpy as np


def main():
	series = read_csv('/home/akshit/Documents/Downloads/2.csv', header=0, index_col=0, squeeze=True)
	series.columns = ['a', 'b', 'c', 'd']
	series['e'] = pow((series['a']*series['a'] + series['b']*series['b'] + series['c']*series['c']), 0.5)

	df = pd.DataFrame({'$a': series['e']})


	fd = np.array(df)
	#mn_for_trailing_fd_for_centered
	mn = fd
	#original_plot
	plt.plot(fd)


	#Centered_Averaging

	for x in range(0, len(fd)-1):
		if(x>=2 and x<=137990): 
			fd[x]=(fd[x-2]+fd[x-1]+fd[x]+fd[x+1]+fd[x+2])/5
	#after_centered
	print("asdasd")
	plt.plot(fd)
	plt.show()
	#Trailing_Moving_Average
	for x in range(0, len(fd)-1):
		if(x>=2 and x<=137995):
			mn[x] = (mn[x-4] + mn[x-3] + mn[x-2] + mn[x-1] + mn[x])/5

	#after_trailing
	print("Asdqwwe")
	plt.plot(mn)
	plt.show()
if __name__ == '__main__':
	main()