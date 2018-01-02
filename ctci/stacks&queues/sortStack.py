'''
sort a given stack in ascending order (biggest on top) by using only one stack extra 
'''

class Stack:
    def __init__(self):
        self.storage=[]
        self.top=0
    
    def push(self,value):
        self.storage.append(value)
        self.top+=1
    
    def pop(self):
        if (self.isEmpty()):
            return
        elem=self.storage.pop()
        self.top-=1
        return elem
    
    def peek(self):
        return self.storage[self.top-1]
    
    def isEmpty(self):
        return self.top==0

def sortStack(s):
    s2=Stack()
      
    while(not(s.isEmpty())):
        # store top element in temporary variable
        tmp=s.pop()
        # if s2 is not empty; pop and push all elements > tmp from s2 into s and push tmp
        while (not(s2.isEmpty()) and (s2.peek()>tmp)):
            s.push(s2.pop())
        s2.push(tmp)
    print(s2.storage)
    return s2
        
s=Stack()
s.push(9)
s.push(7)
s.push(3)
s.push(6)
s.push(4)
s.push(2)

print(s.storage)
sortStack(s)