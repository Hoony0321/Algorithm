from collections import deque
def solution(s):
    answer = True
    
    stack = deque()
    
    for c in s:
        if c == '(':
            stack.append(c)
        elif c == ')':
            if len(stack) > 0 and stack[-1] == '(':
                stack.pop()
            else:
                return False

    return True if len(stack) == 0 else False