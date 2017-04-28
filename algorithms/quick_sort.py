# -*- coding: utf-8 -*-
"""
Created on Thu Apr 13 10:55:34 2017

@author: jasmine
"""

""" Quick Sort """

def quick_sort(l,p,r):
    if(p<r):
        q=partition(l,p,r)
        print('start',p)
        print('mid',q)
        print('end',r)
        quick_sort(l,p,q-1)
        quick_sort(l,q+1,r)

def partition(l,p,r):
    pivot=l[r]
    i=p-1
    for j in range(p,r):
        if(l[j]<pivot):
            i+=1
            l[j],l[i]=l[i],l[j]
    l[i+1],l[r]=l[r],l[i+1]
    return i+1
    
l=[8,3,2,1,12,56,45,32]
r=len(l)-1
quick_sort(l,0,r)
print(l)
    