#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 23 00:05:19 2017

@author: jasmine
"""

from collections import defaultdict

class Graph():
    def __init__(self, graph=None):
        self.graph = defaultdict(set)
    
    def add_edge(self,edge):
        self.graph[edge[0]].add(edge[1])
        self.graph[edge[1]].add(edge[0])
        
    def __str__(self):
        edges=" "
        for keys in self.graph:
            edges+=" " + str(keys) + "->" +  str(self.graph[keys]) 
        return edges
    
    def hasPathDFS(self,s,d):
        visited=set()
        return self.PathDFS(s,d,visited)
    
    def PathDFS(self,s,d,visited):
        if (s in visited):
            return False
        visited.add(s)
        if(s==d):
            return True
        for child in self.graph[s]:
            if (self.PathDFS(child,d,visited)):
                return True
        return False
    
    def hasPathBFS(self,s,d):
        nextToVisit=[]
        visited=[]
        
        nextToVisit.append(s)
        while(nextToVisit!=[]):
            v=nextToVisit.pop(0)
            if(v==d):
                return True
            if (v in visited):
                continue
            visited.append(v)
            
            for child in self.graph[s]:
                nextToVisit.append(child)
        return False
            
        

g=Graph()
g.add_edge(('a','b'))
g.add_edge(('c','d'))
g.add_edge(('a','e'))
print(g)
print(g.hasPathDFS('b','e'))
print(g.hasPathBFS('b','e'))
print(g.hasPathBFS('a','b'))