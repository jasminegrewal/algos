def isvalid1(string):
    dict1={'(':')','[':']','{':'}'}
    stack=[]

    for i in range(0,len(string)):
        print(stack)
        j=len(stack)
        print(string[i])
        if(string[i]=='(' or string[i]=='[' or string[i]=='{'):
            stack.append(string[i])
        elif(string[i]==')' or string[i]==']' or string[i]=='}'):
            if(stack==[]):
                return False
            if((string[i])==(dict1[stack[j-1]])):
                stack.pop()
                '''del stack[j-1]'''
        else:
            return False
    if(stack==[]):
        return True
    else:
        return False
        
""" s1='[()]{}{[()()]()}' """
s1='[()]}'
print(isvalid1(s1))
