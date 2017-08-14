# -*- coding: utf-8 -*-
"""
Created on Fri Jun  2 16:19:39 2017

@author: jasmine
"""

def merge(intervals):
    intervals=sorted(intervals)
    print(intervals)
    result=[]
    for interval in intervals:
        if not result:
            result.append(interval)
        else:
            prev=result.pop()
            if prev[1]>interval[0]:
                prev[1]=max(interval[1],prev[1])
                result.append(prev)
            else:
                result.append(prev)
                result.append(interval)
    return (result)

intervals=[[1,4],[1,5],[3,4]]
print(*merge(intervals),sep=',')
