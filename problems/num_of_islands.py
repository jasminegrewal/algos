# -*- coding: utf-8 -*-
"""
Created on Sun May 21 06:49:43 2017

@author: jasmine
"""
def neighbors(m,i,j):
    print('here',i,j)
    if (i>=0 and i< len(m) and j>=0 and j<len(m[0])):
        if m[i][j] ==1:
            return True
        else:
            return False
    else:
        return False
    
def do_dfs(m,i,j,visited):
    rowNbr = [-1, -1, -1,  0, 0,  1, 1, 1];
    colNbr = [-1,  0,  1, -1, 1, -1, 0, 1];
    if visited[i][j]==True:
        return
    visited[i][j]=True
    for k in range(8):
        if neighbors(m,i+rowNbr[k], j+colNbr[k],visited):
            do_dfs(m,i+rowNbr[k], j+colNbr[k], visited)

def no_islands(m):
    rows=len(m)
    cols=len(m[0])
    count=0
    visited =[[False for j in range(len(m[0]))]for i in range(len(m))]
    for i in range(rows):
        for j in range(cols):
            print('main',i,j)
            if((m[i][j]==1) and (visited[i][j]==False)):
                do_dfs(m,i,j,visited)
                count+=1
    return count
                
m=[[1,0,1,0,1],
   [1,1,0,0,0],
   [0,1,0,1,1]]
print(m)
print(no_islands(m))
