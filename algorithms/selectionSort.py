#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 28 11:43:12 2017

@author: jasmine
"""

def selectionSort(arr):
    for i in range(len(arr)-1):
        # i will go from 0 tp second last element
        min_i=i
        #j will go from i+1 to last element
        for j in range(i+1,len(arr)):
            if(arr[j]<arr[min_i]):
                min_i=j
        #if(min_i!=i):
        print(min_i)
        arr[i],arr[min_i]=arr[min_i],arr[i]
    return arr

numbers=[4,3,5,2,7,0,1]
print(selectionSort(numbers))