# -*- coding: utf-8 -*-
"""
Created on Thu Mar 30 12:28:09 2017

@author: jasmine
"""

def reverse(str1):
    rv=[]
    rv.extend(str1)
    return ''.join(rv[::-1])
    
str1='abcdf'
print(reverse(str1))

''' end=str1[m-1]
    start=str1[0]'''
    
    
        