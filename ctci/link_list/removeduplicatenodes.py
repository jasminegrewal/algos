# -*- coding: utf-8 -*-
"""
Created on Sat May  6 09:17:10 2017

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
    
    def remdup(self):
        nodes=set()
        prev=self.head
        nodes.add(prev.data)
        current=prev.next
        while(current!=None):
            if current.data not in nodes:
                nodes.add(current.data)
                prev=prev.next
            else:
                prev.next=current.next
            current=current.next
    
    def remdupnobuffer(self):
        current=self.head
        while(current!=None):
            runner=current
            while(runner.next!=None):
                if(runner.next.data==current.data):
                    runner.next=runner.next.next
                else:
                    runner=runner.next
            current=current.next
    
    def __str__( self ) :
        link_list = ""
        node = self.head
        if node != None :	
            while node.next != None :
                link_list += str(node.data)
                node = node.next
            link_list += str(node.data)
        return link_list

l=LinkedList()
l.add('i')
l.add('p')
l.add('p')
l.add('s')
l.add('s')
l.add('i')
l.add('s')
l.add('s')
l.add('i')
l.add('m')
print(l)
l.remdup()
print(l)
