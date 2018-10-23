import numpy as np
import matplotlib.pyplot as plt
from numpy.fft import fft,fftfreq, ifft
import csv
import sys
import math

def main():
  d=0; #take d also as input
  #load a data y
  y = []
  print("enter the name of the file")
  file_name = input()
  with open(file_name,'r+') as f:
      reader = csv.reader(f,delimiter = ' ', quotechar='|')
      for number in reader:
         y.append(number[d])
  q=y


  #defining charachteristics of y
  y = np.asarray(y, dtype=float)
  n=y.shape[0]




  #l is total time of measurement, take input
  print("Enter the sampling rate (integer) at which the reading was taken")
  l1=int(input())
  print("Enter the sampling rate (integer) at which you want the FFT to be done, in case of doubt enter the sampling rate you entered previously for observing results")
  l2=int(input())
  if(l2-l1< 0):
     print("FFT cannot be performed at a sampling lower that that of the collected data")
     sys.exit(1)


  #getting altered list
  temp_temp=[]
  p=list(y)

  list_empty=[]
  for j in range(0,l2-l1):
     temp_temp.append(d)
  p_temp=p
  while(len(p_temp) != 0):
     if(len(p_temp) < l1):
        temp=p_temp
        for k in range(0,l2-len(p_temp)):
           temp.append(d)
        p_temp=[]     
     else:   
        temp=p_temp[0:l1]
        p_temp=p_temp[l1:]
        temp+= temp_temp        
     list_empty+=temp
  p=list_empty
  y=np.asarray(p,dtype=float)
  l=l2



  #FFT
  x=np.linspace(0,l,n);
  freq=fftfreq(l)
  mask=freq>0
  y_temp=y
  y2=np.zeros(l,dtype=float)
  r=0
  while(len(y_temp) != 0):
     r=r+1
     y_temp_temp= y_temp[:l]
     y_temp=y_temp[l:]
     y1=fft(y_temp_temp)
     y2_temp=2*np.abs(y1/n)
     y2+=y2_temp

  y2=y2/r

  #Graph
  Label = 'Original data'
  plt.figure(1)
  plt.title('Original Image from Accelerometer')
  plt.plot(x,q,color='xkcd:salmon',label=Label)
  plt.legend()

  plt.figure(2)
  plt.title('FFT')
  plt.plot(freq[mask],y2[mask],label='true fft values')
  plt.show()
