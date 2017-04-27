# -*- coding: utf-8 -*-
"""
Created on Sun Apr 16 11:49:27 2017

@author: jasmine
"""

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self,head=None):
        self.head=head
        
    def add(self,data):
        node=Node(data)
        if(self.head==None):
            self.head=node
        else:
            current=self.head
            node.next=current
            self.head=node
            
    def find(self,data):
        current=self.head
        while (current):
            if current.data==data:
                return current.data
            current=current.next
    
    def remove(self,data):
        prev=self.head
        if(prev.data==data):
            self.head=prev.next
            return
        while (prev.next!=None):
            current=prev.next
            if(current.data==data):
                prev.next=current.next
                break
            else:
                prev=prev.next
        print('not in list')
    
    def __str__( self ) :
        link_list = ""
        node = self.head
        if node != None :	
            while node.next != None :
                link_list += str(node.data)
                node = node.next
            link_list += str(node.data)
        return link_list

n= Node(2)
l=LinkedList(n)
l.add(3)
l.add(4)
l.add(5)
l.find(3)
print(l)
l.remove(2)
print(l)