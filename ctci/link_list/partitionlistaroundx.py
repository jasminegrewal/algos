# -*- coding: utf-8 -*-
"""
Created on Tue May  9 11:14:53 2017

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
        
def partition(l,x):
    current=l.head
    runner=current.next
    while(runner!=None):
        if(current.data>x):
            if(runner.data<x):
                current.data,runner.data = runner.data,current.data
                current=current.next
            #runner=runner.next
        else:
            current=current.next
        runner=runner.next

n= Node(2)
l=LinkedList(n)
l.add(4)
l.add(5)
l.add(3)
l.add(7)
l.add(8)
print(l)   
partition(l,6)
print(l)        