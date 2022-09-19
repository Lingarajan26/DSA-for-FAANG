def linearsearch(arr, searchelemet, n):
	for i in range(n):
		if arr[i]==searchelement:
			return arr[i]	
	return -1
	
arr=[3,5,7,9,12,34]
searchelement=10
n=len(arr)
result=linearsearch(arr,searchelement,n)
print(result)