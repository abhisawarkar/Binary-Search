#!/bin/python
def find_element(arr,start,end,element):

	if end-start >= 0:
		
		mid = (start+end)/2
		if arr[mid] == element:
		        return mid
	
		if arr[mid] < element:
			find_element(arr,mid+1,end,element)
		else:
			find_element(arr,start,mid-1,element)	

	else:
		return -1

arr=[16,32,48,64,80,96,100]
print find_element(arr,0,len(arr)-1,100) 
