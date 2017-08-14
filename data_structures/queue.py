#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 12 06:47:43 2017

@author: jasmine
"""

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
    
class Queue:
    def __init__(self,head=None,tail=None):
        self.head=head
        self.tail=tail

    def isEmpty(self):
        return(self.head==None)
    
    def peek(self):
        if (self.head==None):
            return 
        return(self.head.data)
    
    def add(self,data): 
        node=Node(data)
        if(self.tail!=None):
            self.tail.next=node
        self.tail=node
        if(self.head==None):
            self.head=node
            
    def remove(self):
        if self.head==None:
            return
        data=self.head.data
        self.head=self.head.next
        if(self.head==None):
            self.tail=None
        return data
    
    def __str__(self):
        queue = ""
        node = self.head
        if node != None :	
            while node.next != None :
                queue += " " + str(node.data)
                node = node.next
            queue += " " + str(node.data)
        return queue

    
q=Queue()
print("empty")
print(q.isEmpty())
print(q.peek())
q.add(3)
print(q)
q.add(5)
q.add(1)
q.add(7)
print("empty")
print(q.isEmpty())
print(q)
print("peek")
print(q.peek())
q.remove()
print("empty")
print(q.isEmpty())
print("peek")
print(q.peek())
print(q)
q.remove()
print(q)
q.add(9)
q.add(2)
q.add(11)
print(q)
q.remove()
print(q)
print("peek")
print(q.peek())
print("empty")
print(q.isEmpty())


                
        
        