# -*- coding: utf-8 -*-
"""
Created on Mon Jan 11 09:17:04 2021

@author: hp
"""

import matplotlib.pyplot as pt
import numpy as np
m=n=256
r=20
img=np.zeros([m,n],dtype=np.uint8)
k=10
while k<=101:
    for i in range(0,m):
        for j in range(0,n):
            if (i-128)**2+(j-128)**2<=k**2 and (i-128)**2+(j-128)**2>= k**2 -(2*k):
                img[i,j]=255
    k+=10
pt.imshow(img,cmap="binary")

