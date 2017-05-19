# -*- coding: utf-8 -*-
"""
Created on Fri Mar 24 15:30:31 2017

@author: jasmine
if one str is permutation of other
"""
'''method 1
def ispermut(s1, s2):
    if len(s1)!=len(s2):
        return False
    if ((''.join(sorted(s1))) == (''.join(sorted(s2)))):
        return True
    else:
        return False
        
print (ispermut('abcc','abc'))

'''
def ispermut(s,t):
    if len(s)!=len(t):
        return False
    letters = [0 for i in range(0,128)]
    for char in s:
        letters[ord(char)]=letters[ord(char)]+1
        print(letters)
    for char in t:
        j= ord(char)
        print(letters[j]-1)
        if ((letters[j]-1)<0):
            return False
    return True
        
        
        
print (ispermut('abcc','abcc'))
    
    
    
    

