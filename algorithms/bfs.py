# -*- coding: utf-8 -*-
"""
Created on Thu May  4 18:39:33 2017

@author: jasmine
"""
from collections import deque

def bfs(graph,s):
        visited=set()
        q=deque([])
        q.append(s)
        visited.add(s)
        while q:
            u=q.popleft()
            print('u',u)
            for v in graph[u]-visited:
                #if v not in visited:
                #print('v',v)
                q.append(v)
                visited.add(v)
                #print('visited',visited)
                #print('queue',q)
        return visited
                    
graph = {'A': set(['B', 'C']),
         'B': set(['A', 'D', 'E']),
          'C': set(['A', 'F']),
          'D': set(['B']),
          'E': set(['B', 'F']),
          'F': set(['C', 'E'])}

print(bfs(graph,'A'))
