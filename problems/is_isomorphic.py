"""
Created on Sun Jun  4 22:40:04 2017

@author: jasmine
"""
from collections import defaultdict
def isomorphic(s1,s2):
    mapping=defaultdict(str)
    
    if(len(s1)!=len(s2)):
        return False
    
    for i in range(len(s1)):
        if s1[i] in mapping:
            if mapping[s1[i]]!=s2[i]:
                return False
        else:
            if s2[i] not in mapping.values():
                mapping[s1[i]]=s2[i]
            else:
                return False
     
    return True

s1='paper'
s2='title'
print(isomorphic(s1,s2))
