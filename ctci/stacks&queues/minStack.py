'''
implement a stack which also has a min function to return min
push, pop and min operations operate in O(1) time
'''
import sys

class minStack:
    def __init__(self):
        self.storage=[]
        self.minStorage=[]
        self.top=len(self.storage)-1
    
    def getMin(self):
        if (self.minStorage==[]):
            return sys.maxsize
        return self.minStorage[len(self.minStorage)-1]
        
    def push(self,value):
        self.storage.append(value)
        if (value<=self.getMin()):
            self.minStorage.append(value)
        
    def pop(self):
        if (self.storage.pop()==self.getMin()):
            self.minStorage.pop()
    
    def peek(self):
        return self.storage[self.top]

minStack=minStack()
minStack.push(9)
print("min 9")
print(minStack.getMin())
minStack.push(8)
print("min 8")
print(minStack.getMin())
minStack.push(7)
minStack.push(6)
print("min 6")
print(minStack.getMin())
minStack.pop()
minStack.pop()
print("min 8")
print(minStack.getMin())
