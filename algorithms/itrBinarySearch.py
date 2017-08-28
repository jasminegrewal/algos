#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 28 11:02:38 2017

@author: jasmine
"""

def itrBinarySearch(arr,target):
    left=0
    right=len(arr)-1
    while(left<=right):
        mid=int((left+right)/2)
        if(arr[mid]==target):
            return True
        elif(target<arr[mid]):
            right=mid-1
        else:
            left=mid+1
    return False
    
L = ["Brian", "Joe", "Lois", "Meg", "Peter", "Stewie"]
print(itrBinarySearch(L,"Megan"))