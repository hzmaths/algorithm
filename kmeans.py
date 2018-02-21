# -*- coding: utf-8 -*-
"""
Created on Sun Feb  5 23:06:07 2017

@author: deeplearning
"""

# -*- coding: utf-8 -*-
"""
Created on Sun Feb  5 22:41:40 2017

@author: deeplearning
"""
from matplotlib import pyplot as plt
import numpy as np
k=3
X1=np.random.random((100,3))+10
X2=np.random.random((100,3))+20
X3=np.random.random((100,3))+30
X=np.concatenate((X1,X2,X3),axis=0)
N=X.shape[0]
d=X.shape[1]

c=np.random.choice(N,k)

centers=X[c,:]


print(centers)
dist=np.zeros((X.shape[0],k))
loop=0
while loop<100:
    for i in range(k):
        for j in range(N):
            dist[j,i]=np.sum((X[j]-centers[i,:])**2)
    dist_min=np.argmin(dist,axis=1)
    cen=np.zeros((k,d))
    for i in range(k):
        num=0
        for j in range(N):
            if(i==dist_min[j]):           
                cen[i]+=X[j]
                num+=1
        if num!=0:
            centers[i]=cen[i]/num    
    loop+=1
    
print(centers)
    
                                                 