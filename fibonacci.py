#!/usr/bin/env python

def fibonacci(n):
	if n==0 or n==1:return 1
	else:return fibonacci(n-1)+fibonacci(n-2)

if __name__=="__main__":
	for i in range(20):
		print(fibonacci(i))
