#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 28 14:31:26 2017

@author: jasmine
"""

def quickSort(arr,left,right):
    if(left>=right):
        return
    pivot=arr[int((left+right)/2)]
    index=partition(arr,left,right,pivot)
    quickSort(arr,left,index-1)
    quickSort(arr,index,right)
    
def partition(arr,left,right,pivot):
    while(left<=right):
        while(arr[left]<pivot):
            left+=1
        while(arr[right]>pivot):
            right-=1
        if(left<=right):
            arr[left],arr[right]=arr[right],arr[left]
            left+=1
            right-=1
    return left

numbers=[5,2,6,4,7,9,3]
quickSort(numbers,0,len(numbers)-1)
print(numbers)