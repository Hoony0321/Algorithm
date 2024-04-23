from collections import deque

def solution(n, computers):
    answer = 0
    visited = [False for _ in range(n)]
    
    for i in range(n):
        if visited[i]: continue
        stack = deque()
        stack.append(i)
        visited[i] = True
        
        while stack:
            computer = stack.pop()
            
            for num in range(n):
                if computers[computer][num] == 0: continue
                if visited[num]: continue
                
                stack.append(num)
                visited[num] = True
                
        answer += 1
        
    return answer