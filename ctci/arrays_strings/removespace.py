# -*- coding: utf-8 -*-
"""
Created on Fri Mar 24 17:13:21 2017

@author: jasmine
"""

def removspac(string):
        string=string.strip()
        res=[]
        
        for char in string:
            if (char==' '):
                res +='%20'
            else:
                res += char
        
        print(''.join(res[::]))
        
removspac('   Mr John Smith   ')

def replacesp(instr, l):
    spacecount=0
    newl=0
    for char in instr:
        if (char==' '):
            spacecount +=1
    newl=l+spacecount*2
    print(newl)
    r=[None]*newl
    print(r)
    
    for char in reversed(instr):
        if (char == ' '):
            r[newl-1]='0'
            r[newl-2]='2'
            r[newl-3]='%'
            newl=newl-3
            print(r)
        else:
            r[newl-1]=char
            newl=newl-1
            print(r)
    print(''.join(r[::]))
    
replacesp('   Mr John Smith   ',13)
    
        
    
    
    