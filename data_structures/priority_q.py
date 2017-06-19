# -*- coding: utf-8 -*-
"""
Created on Sat Jun  3 13:33:10 2017

@author: jasmine
"""

class PriorityQueue():
    def __init__(self):
        self.heap=[]
        
    def bubbleUp(self,i):
        while(i>0 and self.heap[i]<self.heap[int(i/2)]):
            self.heap[i],self.heap[int(i/2)]=self.heap[int(i/2)],self.heap[i]
            i=int(i/2)
            
    def insert(self,value):
        self.heap.append(value)
        i=len(self.heap)-1
        self.bubbleUp(i)
        print('append',self.heap)
        
    def bubbleDown(self,i):
        print(i)
        left=2*i+1
        right=2*i+2
        mini=i
        if(left<len(self.heap) and self.heap[left]<self.heap[mini]):
            mini=left
        if(right<len(self.heap) and self.heap[right]<self.heap[mini]):
            mini=right
        if(mini!=i):
            self.heap[mini],self.heap[i]=self.heap[i],self.heap[mini]
            self.bubbleDown(mini)
        
    def extractMin(self):
        min_value=self.heap[0]
        new_top=self.heap.pop()
        if(len(self.heap)!=0):
            self.heap[0]=new_top
            self.bubbleDown(0)
        print('delete',self.heap)
        return min_value
    
    def getMin(self):
        return self.heap[0]

pq=PriorityQueue()
pq.insert(8)
pq.insert(5)
pq.insert(9)
pq.insert(2)
pq.insert(4)
pq.insert(5)
pq.insert(7)
pq.insert(0)
pq.insert(3)
pq.extractMin()
pq.extractMin()
pq.extractMin()
pq.extractMin()
pq.insert(22)
pq.insert(19)
pq.insert(15)
pq.insert(18)
pq.insert(21)
pq.extractMin()
pq.extractMin()
print(pq.getMin())
