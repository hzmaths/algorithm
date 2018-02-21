#!/usr/bin/env python

def search(L,e):
	for i in range(len(L)):
		if L[i]==e:
			return True
	for i in range(len(L)):
		if L[i]==e:
			return True
		if L[i]>e:
			return False;
	return False

if __name__=='__main__':
	L=[1,2,3,4,5,9,8,7]
	L.sort()
	for l in L:
		print(l)

        print(search(L,10))
	print(search(L,5))
