def quicksort(a):
    if len(a)==0:
        return []
    elif len(a) == 1:
        return a
    else:
        pre=[x for x in a if x<a[0]]
        mid=[x for x in a if x==a[0]]
        last=[x for x in a if x>a[0]]
        return quicksort(pre)+mid+quicksort(last)

print(quicksort([1,9,2,7,3,5,36,31]))
