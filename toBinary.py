'''
to Binary form
'''
def toBinary(n):
	bi=''
	while n>0:
		bi=str(n%2)+bi
		n=n/2
	return bi

if __name__ =='__main__':
	print('the binary form of 1024 is ',toBinary(1024))
	print('the binary form of 1025 is ',toBinary(1025))
