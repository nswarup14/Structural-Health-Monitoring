import numpy as np
from matplotlib import pyplot
from statsmodels.tsa.arima_model import ARIMA
from sklearn.metrics import mean_squared_error
import os.path
from pandas import read_csv
import scipy

def checkPath(path_input):
	if os.path.exists(path_input):
		return True
	else:
		return False


def main():
	series = read_csv('file.csv', header=0,delimiter = ' ')
	print(series)
	print(type(series))
	x = list(series.values)
	#x[0][0] = int(x[0][0])
	#x.append(series[0])
	print((x[0][0]))
	x[0][0] = x[0][0].split(',')
	x[0][0] = list(x[0][0])
	#x[0][0].replace("'", "")
	#x[0][0] = list(x[0][0])
	print(type(x[0][0]))
	#print(sum(x[0][0])/len(x[0][0]))
	size = int(len(x) * 0.66)
	sum = 0
	for a in x[0][0]:
	    sum = sum + int(a)
	print(sum/len(x[0][0]))
	#print(size)
	train, test = x[0:size], x[size:len(x)]
	print(train[0][0])

	#print(train[0][0])
	data = []
	#data.append(np.mean(train, axis= 1,dtype = np.ndarray))
	#print(data)

       



