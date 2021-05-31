import numpy as np
import sys

def Bombel(array):

	n=len(array)

	for i in range(n-1):

		for j in range(n-i-1):
			if array[j]>array[j+1]:
				array[j],array[j+1] = array[j+1],array[j]



a = int(sys.argv[1])
b = int(sys.argv[2])
c = int(sys.argv[3])

array=np.random.randint(b,c,size=a)
Bombel(array)

for i in range(len(array)):
	print(array[i])
