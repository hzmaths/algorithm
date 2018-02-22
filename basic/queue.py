#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 22 00:58:27 2018

@author: deeplearning
"""
from node import Node
from emptyexception import EmptyException
class Queue:
    def __init__(self,head = None,tail = None,length = 0):
        self.head = head
        self.tail = tail 
        self.length = length
    
    def is_empty(self):
        return self.head is None
    
    def enqueue(self,item):
        new_node = Node(item,None)
        if self.is_empty():
            self.head = new_node
        else:
            self.tail.next = new_node
        self.tail = new_node
        self.length += 1
    
    def dequeue(self):
        if self.is_empty():
            raise EmptyException('this queue is empty')
        res = self.head.item
        self.head = self.head.next
        self.length -= 1
        if self.size() == 0:
            self.tail = None
        return res
        
    def size(self):
        return self.length
    
if __name__ == '__main__':
    queue = Queue(None,None,0)
    print(queue.is_empty(),queue.size())
    queue.enqueue('1,2,3')
    print(queue.is_empty(),queue.size())
    queue.enqueue('python')
    queue.enqueue('python AI')
    print('tail = ',queue.tail.item)
    head = queue.head
    while head is not None:
        print(head.item)
        head = head.next
    print(queue.is_empty(),queue.size())
    print(queue.dequeue(),queue.is_empty(),queue.size())
    print(queue.dequeue(),queue.is_empty(),queue.size())
    print(queue.dequeue(),queue.is_empty(),queue.size())


   

    