from collections import deque

def solution(n, edges):
    answer = 0
    graph = [[] for _ in range(n+1)]
    
    for edge in edges:
        u,v = edge
        graph[u].append(v)
        graph[v].append(u)
    
    visited = set()
    visited.add(1)
    queue = deque()
    queue.append(1)
    
    while queue:
        answer = 0
        for _ in range(len(queue)):
            curNode = queue.popleft()
            answer += 1
            
            for nearNode in graph[curNode]:
                if nearNode in visited:
                    continue
                queue.append(nearNode)
                visited.add(nearNode)
    
    return answer