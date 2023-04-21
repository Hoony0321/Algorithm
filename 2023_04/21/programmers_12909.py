#문제정보
#programmers_12909 - 올바른 괄호 (난이도 2)

from collections import deque
def solution(s):
    stack = deque()
    
    for char in s:
        stack.append(char)
        
        while len(stack) > 1:
            if (stack[-2] == "(" and stack[-1] == ")"):
                stack.pop()
                stack.pop()
            else:
                break
    
    return True if not stack else False