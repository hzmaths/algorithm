# -*- coding: utf-8 -*-
"""
Created on Wed Dec  7 09:21:49 2016

@author: deeplearning
"""
rang=range(100)
for i in rang:
    print(i)
    
rang2=range(100,300)
for i in rang2:
    if i%5==0:
        print(i)
        
def toBinary(x):
    binary=""
    while(x>=1):
        binary=str(x%2)+binary
        x=x/2;
    return binary

print(toBinary(64))
print(toBinary(100))
print(toBinary(2))

arr=[1,2,6,8,10,45,23,56,3,4,6,8,0]
def quicksort(a):
    if(len(a)<=1):
        return a
    pivot=a[len(a)/2]
    left=[x for x in a if x<pivot]
    mid=[x for x in a if x==pivot]
    right=[x for x in a if x>pivot]
   
    return quicksort(left)+mid+quicksort(right)
    
so=quicksort(arr)
for i in so:
    print(i)
    
map={1:"a",2:"b"}
key=map.keys()
key.append(3)
print(key)
v=map.values
print(v)
for k in key:
    print(map.get(k,"N/A"))
    
class cat:
    def __init__(self,name):
        self.name=name
    def greet(self,greets):
        print(greets)

smallcat=cat("small cat")
smallcat.greet("hello")

import numpy as np

        
        