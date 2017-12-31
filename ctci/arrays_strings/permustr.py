# -*- coding: utf-8 -*-
"""
Created on Fri Mar 24 15:30:31 2017

@author: jasmine
if one str is permutation of other
"""
def ispermut(s,t):
    if len(s)!=len(t):
        return False
    # create an int array of len 128(ASCII) with default  0
    letters = [0 for i in range(0,128)]
    for char in s:
        letters[ord(char)]=letters[ord(char)]+1
    for char in t:
        j= ord(char)
        print(letters[j]-1)
        # if a different char comes values is -1 or if a character count differs value gets negative
        # also we are checking length initially
        if ((letters[j]-1)<0):
            return False
    return True
           
print (ispermut('abcc','abcd'))
