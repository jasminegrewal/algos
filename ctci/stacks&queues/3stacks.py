#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 29 10:46:52 2017

@author: jasmine
"""

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
    
class Stack:
    def __init__(self,top1=None,top2=None,top3=None):
        self.top1=top1
        self.top2=top2
        self.top3=top3
        
    def isEmpty(self):
        return (self.top1==None or self.top2==None or self.top3==None)
    
    def peek(self):
        peeks=[]
        peeks.append(self.top1.data)
        peeks.append(self.top2.data)
        peeks.append(self.top3.data)
        return peeks
    
    def add(self,data,stackNumber): 
        node=Node(data)
        if(stackNumber==1):
            if(self.top1==None):
                self.top1=node
            else:
                node.next=self.top1
                self.top1=node
                node=Node(data)
        elif(stackNumber==2):
            if(self.top2==None):
                self.top2=node
            else:
                node.next=self.top2
                self.top1=node
            
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