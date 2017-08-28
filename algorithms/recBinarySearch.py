#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 28 10:46:45 2017

@author: jasmine
"""

def recBinarySearch(arr, left, right, target):
    if(left>right):
        return False
    mid=int((left+right)/2)
    if(target==arr[mid]):
        return True
    elif(target<arr[mid]):
        return recBinarySearch(arr,left,mid-1,target)
    else:
        return recBinarySearch(arr,mid+1,right,target)
    return False

numbers=[56,78,89,98,101,112,145]
print(recBinarySearch(numbers,0,len(numbers)-1,154))