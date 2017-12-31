# -*- coding: utf-8 -*-
"""
Created on Thu Mar 30 11:32:12 2017

@author: jasmine
"""
'''s1 is substring of s2'''
def issubstring(str1,str2):
    m=len(str1)
    n=len(str2)
    # substring cannot be larger than string itself
    if m>n:
        return False
    # last substring possible starts at index n-m in str2
    for i in range(0,n-m):
        # j tracks the length of substring as we have to check for that much length at once
        for j in range(i,i+m):
            flag=1
            # j starts with an incremented step everytime in string and substring (str1) starts from 0 everytime (j-i)
            if(str2[j]!=str1[j-i]):
                flag=0
                # break from j loop 
                break
        if (flag==1):
            return True
    return False

# s1='erbottlewa'
# s2='waterbottlewaterbottle'
# print(issubstring(s1,s2))

'''is s1 rotated version of s2? if yes then s1 will be substring of s2s2'''
def isrotated(str1,str2):
    if (len(str1)!=len(str2)):
        return False
    s2=str2+str2
    return issubstring(str1,s2)
        
s1='erbottlewa'
s2='waterbottle'
print(isrotated(s1,s2))
