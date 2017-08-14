# -*- coding: utf-8 -*-
"""
Created on Wed Jun  7 11:54:15 2017

@author: jasmine
"""

def confusion_m(actual_y,predicted_y):
    classes=[]
    for y in actual_y:
        if y not in classes:
            classes.append(y)
    
    n=len(classes)
    cm=[[0]*n for i in range(n)]
    for i in range(len(actual_y)):
        print('i',i)
        cm[classes.index(actual_y[i])][classes.index(predicted_y[i])]+=1
        
    print(classes)
    print(cm)
    
actual_y =    ['cat', 'dog', 'cat', 'goat', 'dog', 'goat']
predicted_y = ['cat', 'cat', 'dog', 'goat', 'dog', 'dog']

confusion_m(actual_y,predicted_y)
