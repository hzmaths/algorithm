#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 22 09:27:13 2018

@author: deeplearning
"""
'''
range(start,end,step):包含start,不包含end,默认一步为1
range(9),默认是range(0,9),包含头，不包含尾，一步为1

当倒序时，start 必须大于end，比如 range(9,0,-1)
for i in range(9,0,-1):
    print(i)
9
8
7
6
5
4
3
2
1

'''
def insertsort(a):
    N = len(a)
    for i in range(1,N):
        j = i
        while j > 0:
            if a[j] < a[j-1]:
                a[j],a[j-1] = a[j-1],a[j]
            else:
                break
            j -= 1
        '''
        for j in range(i,-1,-1):
            if a[j] < a[j-1]:
                a[j],a[j-1] = a[j-1],a[j]
        '''
                
if __name__ == '__main__':
    a = [1,7,8,9,3,4,5,100]
    insertsort(a)
    print(a)