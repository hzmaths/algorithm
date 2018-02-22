#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 22 00:11:54 2018

@author: deeplearning
"""

class Node:
    def __init__(self,item,next = None):
        self.item = item
        self.next = next
        


if __name__ == '__main__':
    node = Node('cat',Node('dog',None))
    print(node.next.item)