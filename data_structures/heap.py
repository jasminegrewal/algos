#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 17 09:03:26 2017

@author: jasmine
"""

class MinHeap:
    def __init__(self,items):
        self.items=[]
    
    def getLeftChildIndex(self,i):
        return int(2*i +1)
    
    def getRightChildIndex(self,i):
        return int(2*i +2)
    
    def getParentIndex(self,i):
        return int((i-1)/2)
    
    def hasParent(self,i):
        return (self.getParentIndex(i)>=0)
    
    def hasLeftChild(self,i):
        return (self.getLeftChildIndex(i)<(len(self.items)))
    
    def hasRightChild(self,i):
        return (self.getRightChildIndex(i)<(len(self.items)))
    
    def parent(self,i):
        return (self.items[self.getParentIndex(i)])
    
    def leftChild(self,i):
        return (self.items[self.getLeftChildIndex(i)])
    
    def rightChild(self,i):
        return (self.items[self.getRightChildIndex(i)])
    
    def swap(self,i1,i2):
        self.items[i1],self.items[i2]=self.items[i2],self.items[i1]
    
    def peek(self):
        if (self.items==[]):
            return
        return self.items[0]
        
    def add(self,item):
        self.items.append(item)
        i=len(self.items)-1
        self.heapifyUp(i)
        
    def remove(self):
        if (self.items==[]):
            return
        min_value=self.items[0]
        self.items[0]=self.items.pop()
        self.heapifyDown()
        return min_value
        
    def heapifyUp(self,i):
        while(self.hasParent(i) and self.parent(i)>self.items[i]):
            self.swap(self.getParentIndex(i),i)
            #self.items[i],self.parent(i)=self.parent(i),self.items[i]
            i=self.getParentIndex(i)
        
    def heapifyDown(self):
        i=0
        while(self.hasLeftChild(i)):
            smallChildIndex=self.getLeftChildIndex(i)
            if(self.hasRightChild(i) and self.rightChild(i)<self.leftChild(i)):
                smallChildIndex=self.getRightChildIndex(i)
            
            if(self.items[i]<self.items[smallChildIndex]):
                break
            else:
                self.swap(i,smallChildIndex)
                #self.items[i],self.items[smallChildIndex]=self.items[smallChildIndex],self.items[i]
            i=smallChildIndex
            
    def __str__(self):
        heap=""
        for i in range(len(self.items)):
            heap +=" "+ str(self.items[i])
        return heap
    
            
heap=MinHeap([])
print(heap)
heap.add(25)
heap.add(5)
print(heap.peek())
print(heap)
heap.remove()
print(heap)
heap.add(15)
print(heap)
heap.add(20)
heap.remove()
print(heap)
heap.add(27)
print(heap)
heap.add(2)
print(heap)
heap.remove()
print(heap.peek())
print(heap)
heap.add(9)
print(heap)
heap.add(18)
print(heap.peek())
print(heap)
heap.add(2)
print(heap)
heap.remove()
print(heap)