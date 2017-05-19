# -*- coding: utf-8 -*-
"""
Created on Sat May 13 09:20:09 2017

@author: jasmine
"""

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self,head=None):
        self.head=head
        
    def addhead(self,data):
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

def ispalindrome(l):
    slow=l.head
    fast=l.head
    
    stack=[]
    
    while(fast!=None and fast.next!=None):
        print(fast.data)
        print(slow.data)
        stack.append(slow.data)
        slow=slow.next
        fast=fast.next.next
        
        
        
    print(stack)
    
    if fast!=None: #odd n
        slow=slow.next
        
    while(slow!=None):
        print(stack)
        print(slow.data)
        if(stack.pop()!=slow.data):
            return False
        slow=slow.next
    return True

l=LinkedList()
l.addhead('a')
l.addhead('b')
l.addhead('c')
l.addhead('d')
l.addhead('e')
l.addhead('b')
l.addhead('a')
print(l)
print(ispalindrome(l))