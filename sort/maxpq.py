#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 22 11:35:10 2018

@author: deeplearning
"""
from emptyexception import EmptyException
class MaxPQ:
    def __init__(self):
        self.data = []
        self.N =0
        
    def insert(self,e):
        self.data.append(e)
        self.N += 1
        self.swim(self.N)
        
    def delMax(self):
        if self.size() == 0:
            raise EmptyException('this maxpq is empty')
        qmax = self.data.pop()
        self.data[0],self.data[-1]=self.data[-1],self[0]
        self.sink(1)
        return qmax
    
    def sink(self,k):
        while(2 * k + 1 < self.N):
            j = 2 * k + 1
            if j < self.N - 1 and self.data[j] < self.data[j+1]:
                j += 1
            if self.data[k] > self.data[j]:
                break
            self.data[k],self.data[j] = self.data[j],self.data[j]
            k = j

    def swim(self,k):
        j = (k - 1) // 2
        while j >= 0 and self.data[k] < self.data[j]:
            self.data[k],self.data[j] = self.data[j],self.data[k]
            j = (j - 1) // 2
    def size(self):
        return len(self)