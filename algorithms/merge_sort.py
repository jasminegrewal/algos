# -*- coding: utf-8 -*-
"""
Created on Thu Apr 13 14:54:38 2017

@author: jasmine
"""

"""Merge Sort"""
def merge_sort(arr):
    if (len(arr)<2):
        return arr
        
    mid=int(len(arr)/2)
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left,right)
    
def merge(left,right):
    res=[]
    i,j=0,0
    while(len(res) < len(left) + len(right)):      
        if(left[i]<right[j]):
            res.append(left[i])
            i+=1
        else:
            res.append(right[j])            
            j+=1
        if(i==len(left) or j==len(right)):
            res.extend(left[i:] or right[j:])
    return res

l=[8,3,2,1,12,56,45,32]
print(merge_sort(l))
    