#!/usr/bin/env python

def cube(x):
	return x**3

def applyToEach(L,f):
	for i in range(len(L)):
		L[i]=f(L[i])
        return L
if __name__=='__main__':
	L=[1,2,3,4,5,6]
	print(applyToEach(L,cube))
