# -*- coding: utf-8 -*-
"""
Created on Tue May  9 09:58:03 2017

@author: jasmine
"""

'''find last kth element in singly linked list
last kth element=length(l)-k
go till end of ll, start counting from end
assuming l(1) is last element'''

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

    def kthtolast(self,node,k):
        if(node==None):
            return 0
        i=self.kthtolast(node.next,k) 
        i+=1
        if(i==k):
            print(node.data)
        return i
        
    def kthtolastiter(self,k):
        p1=self.head
        p2=self.head
        for i in range(1,k):
            if(p2==None):
                return None
            p2=p2.next
        if(p2==None):
            return None
        while(p2.next!=None):
            p1=p1.next
            p2=p2.next
        print(p1.data)

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
l.add(4)
l.add(5)
l.add(3)
l.add(7)
l.add(8)
print(l)
l.kthtolastiter(6)