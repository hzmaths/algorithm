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
#整数除法用双斜线//
#####################################################
def quicksort(a):
    N = len(a)
    if N < 2:
        return a
    ind = partition(a)
    #ind = partition2(a)
    return quicksort(a[:ind])+[a[ind]]+quicksort(a[ind+1:])
def partition(a):
    pivot = a[0]
    i,j = 1,len(a)-1
    while True:
        while  a[i] < pivot:
            if i == len(a)-1:
                break
            i += 1
        while  a[j] > pivot:
            if j == 0:
                break
            j -= 1
        if i >= j:
            break
        a[i],a[j] = a[j],a[i]
    a[0],a[j] = a[j],a[0]
    return j           
def partition2(a):
    pivot = a[0]
    i,j = 1,len(a)-1
    while True:
        while i < len(a) and a[i] < pivot:
            i += 1
        while j > 0 and a[j] > pivot:
            j -= 1
        if i >= j:
            break
        a[i],a[j] = a[j],a[i]
    a[0],a[j] = a[j],a[0]
    return j            
if __name__ == '__main__':
    a = [1,7,8,9,3,4,5,100,10000,23,99,4456,88]
    a=quicksort(a)
    print(a)