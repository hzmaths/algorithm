def sqrt2(x):
	epsilon=0.01
	numGuess=0
	low=0
	high=x
	ans=(low + high)/2.0
	while abs(ans**2 -x)>epsilon:
		numGuess+=1
		if ans**2>x:
			high=ans
		else:
			low= ans
		ans=(low+high)/2.0
		print('the ',numGuess,'th answer is ',ans)
	return ans

if __name__=="__main__":
	print(sqrt2(1000))
