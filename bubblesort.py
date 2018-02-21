#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 16 12:12:01 2018

@author: deeplearning
"""

def bubble_sort(a):
    for i in range(len(a)-1):
        j = 0
        while j < len(a) - i - 1:
            if a[j] > a[j+1]:
                a[j],a[j+1] = a[j+1],a[j]
            j += 1
                

a=[3,4,8,9,1,2,3]
bubble_sort(a)
print(a)