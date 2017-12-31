''' return the first node where a loop starts in a linked list'''

class Node:
    def __init__(self,value=None):
        self.value=value
        self.next=None

def firstNodeInCycle(head):
    slow=head
    fast=head
    
    # check if a link list has a loop and stop where two pointers meet
    # meeting point will be loop_size-k steps into the linked list
    # k is size of non-looped part
    while(fast!=None and fast.next!=None):
        fast=fast.next.next
        slow=slow.next
        if(slow==fast):
            break
    
    # if no loop, return None
    if(fast==None or fast.next==None):
        return None
    
    # move slow to head and keep fast at meeting point, now both are k steps from 
    # start of loop. Now they will meet at start of loop
    slow=head
    while(fast!=slow):
        fast=fast.next
        slow=slow.next
    
    return slow.value

head=Node(1)

two=Node(2)
three=Node(3)
four=Node(4)
five=Node(5)
six=Node(6)
seven=Node(7)
eight=Node(8)
nine=Node(9)

head.next=two
two.next=three
three.next=four
four.next=five
five.next=six
six.next=seven
seven.next=eight
eight.next=nine
nine.next=three

print(firstNodeInCycle(head))