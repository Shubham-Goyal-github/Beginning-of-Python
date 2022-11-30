# -*- coding: utf-8 -*-
"""
Created on Wed Dec 16 11:03:01 2020

@author: hp
"""
def insertion_sort(arr):#left part gets sorted
    for i in range(1,len(arr)):
        key=arr[i]
        
        j=i-1
        while j>=0 and key<arr[j]:
            arr[j+1]=arr[j]
            j-=1
        else:
            
            arr[j+1]=key
        print(arr)

arr=[64,34,25,12,22,11,90]
arr1=list(arr)
insertion_sort(arr)
arr1.sort()
print("sorted array: ")
for i in range(len(arr)):
    print(arr[i],arr1[i])
