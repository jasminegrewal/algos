def isvalid(string):
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
print(isvalid(s))
