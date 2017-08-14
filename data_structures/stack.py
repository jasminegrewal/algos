#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 12 07:46:21 2017

@author: jasmine
"""

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
    
class Stack:
    def __init__(self,top=None):
        self.top=top

    def isEmpty(self):
        return (self.top==None)
    
    def peek(self):
        if (self.top==None):
            return
        return (self.top.data)
    
    def add(self,data): 
        node=Node(data)
        node.next=self.top
        self.top=node
            
    def remove(self):
        if self.top==None:
            return
        data=self.top.data
        self.top=self.top.next
        return data
    
    def __str__(self):
        stack = ""
        node = self.top
        if node != None :	
            while node.next != None :
                stack += " " + str(node.data)
                node = node.next
            stack += " " + str(node.data)
        return stack
    
s=Stack()
print(s.isEmpty())
print("peek")
print(s.peek())
s.add(4)
s.add(7)
s.add(8)
print(s)
s.remove()
print(s)
print(s.peek())
print(s.isEmpty())
s.add(3)
s.add(6)
s.add(9)
s.add(2)
s.add(13)
print(s)
s.remove()
print(s)
print(s.peek())
s.add(16)
print(s)
s.remove()
print(s)
print(s.peek())

