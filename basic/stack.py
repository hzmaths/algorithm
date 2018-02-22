#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 22 00:19:38 2018

@author: deeplearning
"""
from node import Node
from emptyexception import EmptyException
class Stack:
    def __init__(self):
        self.first = None
    #top
    
    #isempty
    def is_empty(self):
        return self.first is None
    #push
    def push(self,item):
        new_node = Node(item,self.first)
        self.first = new_node       
    #pop
    def pop(self):
        if self.is_empty():
            raise EmptyException('this stack is empty')
        item = self.first.item
        self.first = self.first.next
        return item
    #top
    def top(self):
        if self.is_empty():
            raise EmptyException('this stack is empty')
        item = self.first.item
        return item
    
    
if __name__ == '__main__':
    stack = Stack()
    print(stack.is_empty())    
    stack.push('abc')
    print(stack.top())
    stack.push('12345')
    print(stack.top())
    stack.pop()
    print(stack.top()) 
    print(stack.is_empty())
    stack.pop()
    print(stack.top())