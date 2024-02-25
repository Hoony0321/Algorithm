from collections import deque

def isValidString(p):
    stack = deque();
    
    for char in p:
        stack.append(char);
        
        while(len(stack) > 1):
            if(stack[-2] == '(' and stack[-1] == ')'):
                stack.pop();
                stack.pop();
                continue
            break
            
    return len(stack) == 0

def separateString(p):
    left = 0
    right = 0
    
    for char in p:
        if(char == '('):
            left += 1
        if(char == ')'):
            right += 1
        
        if(left == right): break
    
    return p[:left+right], p[left+right:]
    
    

def process(w):
    print(w)
    if(len(w) == 0):
        return "";
    
    if(isValidString(w)):
        return w
    
    u,v = separateString(w)
    
    if(isValidString(u)):
        return u + process(v)
    
    result = '('
    result += process(v)
    result += ')'
    
    newU = ''
    for i in range(len(u)-2):
        if(u[i+1] == '('):
            newU += ')'
        else:
            newU += '('
    
    return result + newU    
    

def solution(p):
    return process(p)