#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 28 11:14:37 2017

@author: jasmine
"""

def bubbleSort(arr):
    for i in range(len(arr)-1):
        ''' i will go from 0 to second last element
         last element will be compared at second last position'''
        for j in range((len(arr)-1)-i):
            '''j will go from 0 till n-i^th position as largest element will keep taking their 
            right position and unsorted array will keep decreasing to left
            i.e largest elements will take their position first '''
            if(arr[j]>arr[j+1]):
                arr[j],arr[j+1]=arr[j+1],arr[j]
    return arr

def optimizedSort(arr):
    isSorted=False
    lastUnsorted=len(arr)-1
    while(not isSorted):
        isSorted=True
        for i in range(lastUnsorted):
            if(arr[i]>arr[i+1]):
                arr[i],arr[i+1]=arr[i+1],arr[i]
                isSorted=False
        lastUnsorted-=1
    return arr

numbers=[6,4,7,3,9,1,2,8,0]
#print(bubbleSort(numbers))
print(optimizedSort(numbers))