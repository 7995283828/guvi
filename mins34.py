def smallest(array,n):
	min=array[0]
	for i in range(1,n):
		if array[i]<min:
			min=array[i]
	return min
array=[10,15,6,60,54]
n=len(array)
ans=smallest(array,n)
print("the smallest element of the array is:",ans )
			
