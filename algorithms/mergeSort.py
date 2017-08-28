#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 28 12:30:21 2017

@author: jasmine
"""

def mergeSort(arr,left,right):
    if (left>=right):
        return
    mid=int(((left+right)/2))
    mergeSort(arr,left,mid)
    mergeSort(arr,mid+1,right)
    merge(arr,left,right,mid)
    
def merge(arr,leftStart,rightEnd,mid):
    print(leftStart)
    print(rightEnd)
    L=[]
    R=[]
    size_l=mid-leftStart+1
    size_r=rightEnd-mid
    for i in range(size_l):
        L.append(arr[leftStart+i])
    for j in range(size_r):
        R.append(arr[mid+1+j])
    
    i=0
    j=0
    k=leftStart
    
    while(i<size_l and j<size_r):
        if(L[i]<R[j]):
            arr[k]=L[i]
            i+=1
        else:
            arr[k]=R[j]
            j+=1
        k+=1
    
    while(i<size_l): 
        arr[k]=L[i]
        i+=1
        k+=1
    
    while(j<size_r): 
        arr[k]=R[j]
        j+=1
        k+=1
            
    

numbers=[3,6,5,4,8,9,2,1,0,7]
temp=[]
mergeSort(numbers,0,len(numbers)-1)
print(numbers)
    
            
        