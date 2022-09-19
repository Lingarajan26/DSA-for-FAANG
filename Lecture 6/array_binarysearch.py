def binarysearch(array,i,j,x):
    if i==j:
        if array[i]==x:
            return i
        else:
            return -1
    else:
        print("i value is ",i)
        print("j value is ",j)
        mid=i+(j-i) // 2
        print("x value is ",x)
        print("mid value is ",mid)
        print("Hello1")
        if array[mid]==x:
            print("Hello2")
            return mid
        elif array[mid]<x:
            print("Hello3")
            return binarysearch(array,mid+1,j,x)
        elif array[mid]>x:
            print("Hello4")
            return binarysearch(array,i,mid-1,x)
        else:
            return -1

#Driver code
array=[5,10,13,18,27,36,45,69,94]
i=0
j=len(array)-1
x=int(input("Enter the value you looking for "))
result= binarysearch(array,i,j,x)
print("searching position of the element at",result)