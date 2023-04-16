#문제정보
#programmers_154539 - 뒤에 있는 큰 수 찾기 (난이도2)

from collections import deque

def solution(numbers):
    answer = deque([])
    stack = deque()
    
    for idx in range(len(numbers)-1, -1, -1):
        number = numbers[idx]
        isAppend = False
        
        while stack:
            top = stack[0]
            if(top <= number): #number보다 같거나 작은 경우 -> pop
                stack.popleft()
            else: #number보다 top이 큰 경우 -> 큰 수 찾음.
                answer.appendleft(top)
                stack.appendleft(number)
                isAppend = True
                break
        
        if not isAppend:
            answer.appendleft(-1)
            stack.appendleft(number)
        
    
    return list(answer)