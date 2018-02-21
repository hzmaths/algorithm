#!/usr/bin/env python

def findDivisors(n1,n2):
	divisors=()
	for i in range(1,min(n1,n2)+1):
		if n1%i==0 and n2%i==0:
			divisors=divisors+(i,)
	return divisors

if __name__=='__main__':
        n1=1024*5*5*7
	n2=512*9*5*7
	print('find the divisors of (',n1,',',n2,')')
	for d in findDivisors(n1,n2):
		print(d)
