#!/usr/bin/env python

def bSearch(L,key,low,high):
	if high==low:return L[low]==key
	mid=low+int((high-low)/2)
	if L[mid]==key:return True
	if L[mid]<key:return bSearch(L,key,mid+1,high)
	else : return bSearch(L,key,low,mid-1)
	

if __name__ =='__main__':
	L=[1,2,4,5,7,8]
	L.sort()
        print(bSearch(L,3,0,len(L)-1))
	print(bSearch(L,7,0,len(L)-1))


