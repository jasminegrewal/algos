# -*- coding: utf-8 -*-
"""
Created on Wed Nov  8 11:52:30 2017

@author: jasmine
"""

'''Search in sorted rotated array'''

def search(arr,target):
    start=0
    end=len(arr)-1
    while(start<=end):
        mid=int((start+end)/2)
        if (arr[mid]==target):
            return mid
        if (arr[mid]>arr[start]):
            if arr[start]<=target and arr[mid]>target:
                end=mid-1
            else:
                start=mid+1
        else:                           #arr[mid]<arr[start]
            if arr[mid]<target and arr[end]>=target:
                start=mid+1
            else:
                end=mid-1
    return -1

arr=[7, 8, 9, 10, 1, 2, 3, 4, 5, 6]
print(search(arr,10))