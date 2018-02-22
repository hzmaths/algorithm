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
######################################################
#每次寻找最大，和尾部交换,只记住指标即可
#####################################################
def selectsort(a):
    N = len(a)
    for i in range(N):
        j = i + 1
        ind = i
        while j < N :
            if a[ind] > a[j]:
                ind = j 
            j += 1
        a[ind],a[i] = a[i],a[ind]
                
if __name__ == '__main__':
    a = [1,7,8,9,3,4,5,100]
    selectsort(a)
    print(a)