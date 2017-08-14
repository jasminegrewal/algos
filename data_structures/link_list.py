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
        
    def prepend(self,data):
        newHead=Node(data)
        newHead.next=self.head
        self.head=newHead
        
    def append(self,data):
        if(self.head==None):
            self.head=Node(data)
        curr=self.head
        while(curr.next!=None):
            curr=curr.next
        curr.next=Node(data)
            
    def find(self,data):
        current=self.head
        while (current):
            if current.data==data:
                return current.data
            current=current.next
    
    def removewithValue(self,data):
        if(self.head==None):
            return
        #also covers remove first one case
        if(self.head.data==data):
            self.head=self.head.next
        curr=self.head
        while(curr.next!=None):
            if(curr.next.data==data):
                curr.next=curr.next.next
                return
            curr=curr.next
            
    def __str__( self ) :
        link_list = ""
        node = self.head
        if node != None :	
            while node.next != None :
                link_list += " " + str(node.data)
                node = node.next
            link_list += " " + str(node.data)
        return link_list

n= Node(2)
l=LinkedList(n)
l.append(3)
l.append(4)
l.append(5)
l.prepend(9)
l.append(6)
l.append(7)
l.find(3)
print(l)
l.removewithValue(2)
print(l)
l.removewithValue(7)
print(l)