# -*- coding: utf-8 -*-
"""
Created on Tue Mar 28 09:33:47 2017

@author: jasmine
"""
from collections import Counter
def compress(string):
    op=""
    count=1
    op+=string[0]
    for i in range(0,len(string)-1):
        if(string[i+1]==string[i]):
            count+=1
        else:
            op+=str(count)
            op+=string[i+1]
            count=1
    op+=str(count)    
    return op
    
print(compress("aabccccca"))
s='aabccccca'
sc=Counter(s)
print(sc)
print(*sc, sep='')

    



        
        