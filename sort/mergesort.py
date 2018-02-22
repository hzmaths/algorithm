#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 22 09:27:13 2018

@author: deeplearning
"""
'''
'''
######################################################
#分两块，再合并,
#一定要注意逻辑顺序，
'''
if i < len(a) and j < len(b):
    if a[i] <= b[j]:
        c.append(a[i])
        i += 1
    else :
        c.append(b[j])
        j += 1
elif i == len(a):
    c.append(b[j])
    j += 1
else:
    c.append(a[i])
    i += 1
'''

'''
for (int k = lo; k <= hi; k++)
{
if
(i > mid)
else if (j > hi)
else if (less(aux[j], aux[i]))
else
}


'''
#整数除法用双斜线//
##有一步优化
#####################################################
def mergesort(a):
    N = len(a)
    if N < 2:
        return a
    mid = N // 2
    left = a[:mid]
    right = a[mid:]
    left = mergesort(left)
    right = mergesort(right)
    a = merge(left,right)
    return a

def merge(a,b):
    i = 0
    j = 0
    c = []
    k = 0
    N = len(a) + len(b)
    if a[-1] <= b[0]:
        return a + b
    while k < N:
        if i < len(a) and j < len(b):
            if a[i] <= b[j]:
                c.append(a[i])
                i += 1
            else :
                c.append(b[j])
                j += 1
        elif i == len(a):
            c.append(b[j])
            j += 1
        else:
            c.append(a[i])
            i += 1
        k += 1   
    return c            
if __name__ == '__main__':
    print(merge([1,3,5,7,9],[2,4,6,8]))
    a = [1,7,8,9,3,4,5,100]
    a=mergesort(a)
    print(a)