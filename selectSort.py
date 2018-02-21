#!/usr/bin/env python

def select(L):
	for i in range(len(L)):
		minIndex=i
		minVal=L[i]
		j=i+1
		while j<len(L):
			if minVal>L[j]:
				minVal=L[j]
				minIndex=j
			j=j+1
		temp=L[i]
		L[i]=minVal
		L[minIndex]=temp

if __name__=='__main__':
	L=[2,9,3,6,7]
	select(L)
	for l in L:
		print(l)
			
