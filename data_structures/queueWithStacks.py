#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 14 13:38:34 2017

@author: jasmine
"""
import stack
    
class MyQueue:
    def __init__(self,stackNewestOnTop=None,stackOldestOnTop=None):
        self.stackNewestOnTop=stack.Stack()
        self.stackOldestOnTop=stack.Stack()
    
    def shiftStacks(self):
        if(self.stackOldestOnTop.isEmpty()):
            while not(self.stackNewestOnTop.isEmpty()):
                self.stackOldestOnTop.add(self.stackNewestOnTop.remove())
        
    def enqueue(self,data):
        self.stackNewestOnTop.add(data)

    def dequeue(self):
        self.shiftStacks()
        return self.stackOldestOnTop.remove()
        
    def peek(self):
        self.shiftStacks()
        return self.stackOldestOnTop.peek()
    
q=MyQueue()
q.enqueue(5)
q.enqueue(6)
print(q.peek())
print(q.dequeue())
q.enqueue(7)
print(q.dequeue())
q.enqueue(2)
q.enqueue(4)
print(q.peek())
print(q.dequeue())
q.enqueue(8)
print(q.dequeue())
q.enqueue(9)
print(q.peek())
