# -*- coding: utf-8 -*-
"""
Created on Mon Dec 28 08:45:41 2020

@author: hp
"""

def bubblesort(arr):
    n=len(arr)
    count=0
    #traverse through all elements of array
    for i in range(n-1):
        #range(n) aslo work but outer loop will repaet 1 more time
        #lAst i elements are already in place
        for j in range(0,n-i-1):
            count=count+1
            if arr[j]>arr[j+1]:
                temp=arr[j+1]
                arr[j+1]=arr[j]
                arr[j]=temp
    print(count)
    
arr1=[64,34,25,12,22,11,90]
(bubblesort(arr1))
print('sorted array')


for i in range(len(arr1)):
    print(arr1[i])
    
