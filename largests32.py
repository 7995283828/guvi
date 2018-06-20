def largest(array,n):
	max=array[0]
	for i in range(1,n):
		if array[i]>max:
			max=array[i]
	return max
array=[10,15,6,60,54]
n=len(array)
ans=largest(array,n)
print("the largest element of the array is:",ans )
			
