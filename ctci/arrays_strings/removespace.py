# -*- coding: utf-8 -*-
"""
Created on Fri Mar 24 17:13:21 2017

@author: jasmine
"""
<<<<<<< f2ec9ce8ff264b29cbdb4c954eec2980e269d2c8
def replaceSp(instr, l):
    spacecount=0
    newl=0
    # removing space at the beginning and at the end of the string
=======

def replaceSp(instr, l):
    spacecount=0
    newl=0
>>>>>>> adding new files
    instr=instr.strip()
    for char in instr:
        if (char==' '):
            spacecount +=1
    # newl is the length of the string to be returned
    newl=l+spacecount*2
<<<<<<< f2ec9ce8ff264b29cbdb4c954eec2980e269d2c8
    # r is the character list of new string to be returned
=======
>>>>>>> adding new files
    r=[None]*newl
    
    for char in reversed(instr):
        if (char == ' '):
            r[newl-1]='0'
            r[newl-2]='2'
            r[newl-3]='%'
            newl=newl-3
        else:
            r[newl-1]=char
            newl=newl-1
    print(''.join(r[::]))
    
replaceSp('   Mr John Smith   ',13)

'''If l is not given, only string is given with enough spaces at back to fill with %20'''

def replaceSpace(sentence):
    # reading the string without the extra spaces
    newSentence=sentence.strip()
    # making a list of original string to make changes else item assignment error in string
    sentence=[ch for ch in sentence]
    i=len(sentence)
    for char in reversed(newSentence):
        if(char==' '):
            sentence[i-1]='0'
            sentence[i-2]='2'
            sentence[i-3]='%'
            i-=3
        else:
            sentence[i-1]=char
            i-=1
    return (''.join(sentence[::]))

<<<<<<< f2ec9ce8ff264b29cbdb4c954eec2980e269d2c8
print(replaceSpace('Mr John Smith    '))
=======
print(replaceSpace('Mr John Smith    '))
>>>>>>> adding new files
