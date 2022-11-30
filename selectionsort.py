# -*- coding: utf-8 -*-
"""
Created on Wed Dec 16 10:53:12 2020

@author: hp
"""
arr=[64,34,25,12,22,11,90]
def selection_sort(arr):
    for i in range(len(arr)):
        min_idx=i
        for j in range(i+1,len(arr)):
            if arr[min_idx]>arr[j]:
                min_idx=j
        temp=arr[i]
        arr[i]=arr[min_idx]
        arr[min_idx]=temp
        


selection_sort(arr)
print(arr)
# arr1.sort()
# print("sorted array: ")
# for i in range(len(arr)):
#     print(arr[i],arr1[i])
    