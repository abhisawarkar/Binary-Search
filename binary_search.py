#!/bin/python

def find_element(arr,start,end,element):

	if end-start >= 0:
		
		mid = (start+end)/2		# finds middle element
		if arr[mid] == element:
		        return mid
	
		if arr[mid] < element:
			find_element(arr,mid+1,end,element) 	# check left side 
		else:
			find_element(arr,start,mid-1,element)	# check right side

	else:
		return -1


