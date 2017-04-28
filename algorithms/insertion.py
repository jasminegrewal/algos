# -*- coding: utf-8 -*-
"""
Created on Fri Apr 14 12:59:13 2017

@author: jasmine
"""

'''Insertion Sort'''

def insert_sort(a):
    for j in range(1,len(a)):
        key=a[j]
        i=j-1
        while(i>=0 and a[i]>key):
            a[i+1]=a[i]
            i-=1
        a[i+1]=key
        return a
        
a=[5,35,6,7,34,2,42,1]
print(insert_sort(a))