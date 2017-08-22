#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 17 14:23:16 2017

@author: jasmine
"""

class Node:
    def __init__(self,info=None):
        self.info=info
        self.left=None
        self.right=None
        
class BST:
    def __init__(self,root=None):
        self.root=root
        
    def insert(self,data):
        newNode=Node(data)
        if (self.root==None):
            self.root=newNode
            return
        current=self.root
        while(True):
            parent=current
            if(data<current.info):
                current=current.left
                if current is None:
                    parent.left=newNode
                    return
            else:
                current=current.right
                if current is None:
                    parent.right=newNode
                    return
                
    def find(self,data):
        current=self.root
        while(current is not None):
            if(current.info==data):
                return True
            elif (current.info>data):
                current=current.left
            else:
                current=current.right
        return False
    
    def delete(self,data):
        current=self.root
        isLeftChild=False
        while(current.info!=data):
            parent=current
            if(current.info>data):
                isLeftChild=True
                current=current.left
            else:
                isLeftChild=False
                current=current.right
            if current==None:
                return False
            
        # Node to be deleted has no child
        if(current.left is None and current.right is None):
            if(current==self.root):
                self.root=None
            if(isLeftChild):
                parent.left=None
            else:
                parent.right=None
                
        # Node to be deleted has one child
        elif(current.right is None):   #has left child
            if(current==self.root):
                self.root=current.left
            elif(isLeftChild):
                parent.left=current.left
            else:
                parent.right=current.left
        
        elif(current.left is None):   #has right child
            if(current==self.root):
                self.root=current.right
            elif(isLeftChild):
                parent.left=current.right
            else:
                parent.right=current.right
        
        # Node to be deleted has both left and right child
        elif(current.left is not None and current.right is not None):
            successor=self.getSuccessor(current)
            print("successor")
            print(successor.info)
            if(current==self.root):
                self.root=successor
            elif(isLeftChild):
                parent.left=successor
            else:
                parent.right=successor
            successor.left=current.left
        return True
    
    # returns the smallest node from right subtree to replace the node to be deleted       
    def getSuccessor(self,delnode):
        current=delnode.right
        successor=None
        succparent=None
        while current is not None:
            succparent=successor
            successor=current
            current=current.left
            
        # successor is the smallest/target node at this point
        if (successor!=delnode.right):
            print('here')
            succparent.left=successor.right #can only have right child
            successor.right=delnode.right # as it will replace the delnode
        return successor
        
    def display(self):
        q=[]
        if (self.root is None):
            return
        q.append(self.root)
        while(q!=[]):
            levelNodes=len(q)
            nodes=" "
            for i in range(levelNodes):
                node=q[i]
                nodes+=" "+ str(node.info)
            print(nodes)
            while(levelNodes>0):
                n=q.pop(0)
                if(n.left is not None):
                    q.append(n.left)
                if(n.right is not None):
                    q.append(n.right)
                levelNodes-=1
    
    def inorder(self,node):
        if(node.left is not None):
            self.inorder(node.left)
        print(node.info)
        if(node.right is not None):
            self.inorder(node.right)
    
    def preorder(self,node):
        print(node.info)
        if(node.left is not None):
            self.preorder(node.left)
        if(node.right is not None):
            self.preorder(node.right)
            
    def postorder(self,node):
        if(node.left is not None):
            self.postorder(node.left)
        if(node.right is not None):
            self.postorder(node.right)
        print(node.info)
            
bst=BST()
bst.insert(5)
bst.insert(3)
bst.insert(7)
bst.insert(1)
bst.insert(9)
bst.insert(4)
print('inorder')
bst.inorder(bst.root)
print('preorder')
bst.preorder(bst.root)
print('postorder')
bst.postorder(bst.root)
print(" ")
bst.display()
bst.delete(5)
bst.display()
bst.inorder(bst.root)
