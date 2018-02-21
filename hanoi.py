def move(n,fro,to):
	print('move  from ',fro,' to ',to)

def tower(n,fro ,to ,spare):
	if n==1:move(n,fro,to)
	else:
		tower(n-1,fro,spare,to)	
		tower(1,fro,to,spare)
		tower(n-1,spare,to,fro)

if __name__ =='__main__':
	tower(20,1,3,2)

