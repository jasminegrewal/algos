#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 28 11:58:07 2017

@author: jasmine
"""

def insertionSort(arr):
    #i will go from 0 to second last element
    for i in range(len(arr)-1):
        # last element will be key and second last position of i
        key=arr[i+1]
        while(i>=0 and arr[i]>key):
            arr[i+1]=arr[i]
            i-=1
        arr[i+1]=key
    return arr

numbers=[4,3,5,2,7,0,1]
print(insertionSort(numbers))