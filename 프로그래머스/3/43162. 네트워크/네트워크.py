from collections import deque

def solution(n, graph):
    answer = 0
    
    visited = [False for _ in range(n)]
    
    for i in range(n):
        if visited[i]: continue
        visited[i] = True
        answer += 1
        
        queue = deque()
        queue.append(i)
        
        while queue:
            num = queue.popleft()
            
            for j in range(n):
                if visited[j]: continue
                if graph[num][j] == 0: continue
                
                visited[j] = True
                queue.append(j)
        
        
    
    return answer