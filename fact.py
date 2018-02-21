def fact(n):
	if n==1:return n
	else: return n*fact(n-1)

if __name__=='__main__':
	print('the fractial of 5 is ',fact(5))
