# -*- coding: utf-8 -*-
"""
Created on Thu May  4 19:22:56 2017

@author: jasmine
"""

def dfs(graph,s):
        visited=set()
        stack=[]
        stack.append(s)
        while stack:
            u=stack.pop()
            print('u',u)
            if u not in visited:
                visited.add(u)
                stack.extend(graph[u]-visited)
                print('visited',visited)
                print('stack',stack)
        return visited
                    
graph = {'A': set(['B', 'C']),
         'B': set(['A', 'D', 'E']),
          'C': set(['A', 'F']),
          'D': set(['B']),
          'E': set(['B', 'F']),
          'F': set(['C', 'E'])}

print(dfs(graph,'A'))
