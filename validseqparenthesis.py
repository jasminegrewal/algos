"""Time Complexity: O(n) as it goes to the for loop n number of times (in worst case) when it goes until end of string
Space Complexity: O(n) for creating list which would be adding all chars in string to list in worst case"""
def isValid(string):
    dict1={'(':')','[':']','{':'}'}
    stack=[]
    j=0

    for i in range(0,len(string)):
        print(stack)
        print(string[i])
        if(string[i]=='(' or string[i]=='[' or string[i]=='{'):
            stack.append(string[i])
            j+=1
        elif(string[i]==')' or string[i]==']' or string[i]=='}'):
            if(stack==[]):
                return False
            if((string[i])==(dict1[stack[j-1]])):
                stack.pop()
                j-=1
                '''del stack[j-1]'''
        else:
            return False
    if(stack==[]):
        return True
    else:
        return False
        
s='[()]{}{[()()]()}'
s1='[()]}'
print(isValid(s))
