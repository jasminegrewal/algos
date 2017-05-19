# -*- coding: utf-8 -*-
"""
Created on Tue May  9 11:03:57 2017

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
    
    def __str__( self ) :
        link_list = ""
        node = self.head
        if node != None :	
            while node.next != None :
                link_list += str(node.data)
                node = node.next
            link_list += str(node.data)
        return link_list

def remnode(node):
    if(node==None or node.next==None):
        return False
    runner=node.next
    node.data=runner.data
    node.next=runner.next
    return True
    
l=LinkedList()
l.add(4)
l.add(5)
l.add(3)
l.add(7)
l.add(8)
print(l)
current=l.head
for i in range(1,3):
    current=current.next
print(current.data)
remnode(current)
print(l)