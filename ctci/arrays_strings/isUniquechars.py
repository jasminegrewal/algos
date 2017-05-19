# -*- coding: utf-8 -*-
"""
Created on Fri Mar 24 11:20:07 2017

@author: jasmine
1.1 check if a string has all unique characters
"""
def isUniqueChars(str):
    if len(str)>128:
        return False
        
    arr = [False]*128
    print (arr)
    for char in str:
        if arr[ord(char)] is False:
            arr[ord(char)] = True
        else: return False
    return True

print (isUniqueChars("manu"))
        