# -*- coding: utf-8 -*-
"""
Created on Wed Mar 29 18:52:48 2017

@author: jasmine
"""

def nullify(m):
    row=[False]*len(m)
    col=[False]*len(m[0])
    
    for i in range(0,len(m)):
        for j in range(0,len(m[0])):
            if (m[i][j]==0):
                row[i]=True
                col[j]=True
                
    for b in range(0,len(row)):
        if (row[b]==True):
            for j in range(0,len(m[0])):
                m[b][j]=0
                
    for b in range(0,len(col)):
        if (col[b]==True):
            for j in range(0,len(m)):
                m[j][b]=0
    
    return m
               
m=[[1,2,0,4,7,8],[5,6,7,8,7,9],[2,4,3,0,9,7]] 
print(nullify(m))   
    