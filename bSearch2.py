def search(L, e):
	def bSearch(L, e, low, high):
		if high == low:
			return L[low] == e
		mid = low + int((high - low)/2)
		if L[mid] == e:
			return True
		if L[mid] > e:
			return bSearch(L, e, low, mid - 1)
		else:
			return bSearch(L, e, mid + 1, high)

	if len(L) == 0:
		return False
	else:
		return bSearch(L, e, 0, len(L) - 1)


l=[1,2,3,4,5,6,7]
print(search(l,5))
print(search(l,10))
