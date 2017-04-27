# -*- coding: utf-8 -*-
"""
Created on Tue Apr 18 11:18:04 2017

@author: jasmine
"""

def maxHeapify(a,i,heapSize):
    left=2*i+1
    right=2*i+2
    if (left<heapSize and a[left]>a[i]):
        print('left is max')
        largest=left
    else:
        largest=i
        print('root is max')
    if(right<heapSize and a[right]>a[largest]):
        print('right is max')
        largest=right
    print(largest)
    print(a[largest])
    print(a)
    if(largest!=i):
        a[i],a[largest]=a[largest],a[i]
        maxHeapify(a,largest,heapSize)

'''a=[16,4,10,14,7,9,3,2,8,1]
maxHeapify(a,1,len(a))
print(a)'''

def buildMaxHeap(a):
    for i in range((int((len(a)-1)/2)),-1,-1):
        maxHeapify(a,i,len(a))
        
'''a=[16,4,10,14,7,9,3,2,8,1]
buildMaxHeap(a)
print(a)'''

def heapSort(a):
    buildMaxHeap(a)
    heapSize=len(a)
    for i in range((len(a)-1),0,-1):
        a[0],a[i]=a[i],a[0]
        heapSize -=1
        print('heapSize',heapSize)
        maxHeapify(a,0,heapSize)
        
a=[16,4,10,14,7,9,3,2,8,1]
heapSort(a)
print(a)

        