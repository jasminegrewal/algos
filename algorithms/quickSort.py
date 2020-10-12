#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 28 14:31:26 2017

@author: jasmine
"""

def quicksort(inpt):
    
    def quickhelper(b,e):
        # base case
        if b>=e:
            return 
        pivot=e
        wall=b
        for i in range(b,e):
            if(inpt[i]<inpt[pivot]):
                inpt[i],inpt[wall]=inpt[wall],inpt[i]
                wall+=1
        inpt[wall],inpt[pivot]=inpt[pivot],inpt[wall]
        quickhelper(b,wall-1)
        quickhelper(wall+1,e)
    
    quickhelper(0,len(inpt)-1)
    
    return inpt
