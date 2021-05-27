def Bombel(array):

	n=len(array)

	for i in range(n-1):

		for j in range(n-i-1):
			if array[j]>array[j+1]:
				array[j],array[j+1] = array[j+1],array[j]
array=[1,31,4,2334,5,2,44,32,42,48,46,5,6,567,45,7,8,6,9,632]

Bombel(array)

for i in range(len(array)):
	print(array[i])
