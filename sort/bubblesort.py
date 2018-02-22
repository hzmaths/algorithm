#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 22 09:27:13 2018

@author: deeplearning
"""

def bubblesort(a):
    N = len(a)
    for i in range(N-1):
        for j in range(N-1-i):
            if a[j] > a[j+1]:
                a[j],a[j+1] = a[j+1],a[j]
                
if __name__ == '__main__':
    a = [1,7,8,9,3,4,5,100]
    bubblesort(a)
    print(a)