def median(list1):
	list1.sort()
	a=len(list1)
	if a%2==0:
		b=list1[round(a/2)]
		c=list1[(round(a/2))-1]
		d=(b+c)/2
		return d
	else:
		return list2[round(a/2)-1]
mylist2=[1,4,6,3,5]
mylist1=[5,3,7,1,2,9]
print(median(mylist2))
print(median(mylist1))
