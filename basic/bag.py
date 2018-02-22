#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 22 01:25:36 2018

@author: deeplearning
"""

class Bag:
    def __init__(self):
        self.data = []
    
    def is_empty(self):
        return len(self.data) == 0
    
    def add(self,item):
        self.data.append(item)
    
    def size(self):
        return len(self.data)
    
if __name__ == '__main__':
    bag = Bag()
    bag.add('123')
    print(bag.data,bag.is_empty(),bag.size())
    bag.add('python3.6')
    print(bag.data,bag.is_empty(),bag.size())

    