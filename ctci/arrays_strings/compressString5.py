# -*- coding: utf-8 -*-
"""
Created on Tue Mar 28 09:33:47 2017

@author: jasmine
"""
def compressString(string):
    result=""
    count=1
    result+=string[0]
    for i in range(0,len(string)-1):
        if(string[i+1]==string[i]):
            count+=1
        else:
            result+=str(count)
            result+=string[i+1]
            count=1
    result+=str(count)    
    return ( result if len(result)<len(string) else string)
    
print(compressString("aabccccc"))
print(compressString("abcdegg"))
