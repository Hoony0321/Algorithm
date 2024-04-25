from collections import deque
from copy import deepcopy

def solution(tickets):
    answer = []
    
    tickets.sort(key = lambda x:x[1], reverse=True)
    
    visited = [False for _ in range(len(tickets))]
    stack = deque()
    route = ['ICN']
    
    stack.append(['ICN', visited, route]) # current, visited, count
    
    while stack:
        current, visited, route = stack.pop()
        if(len(route) > len(tickets)):
            return copiedRoute
        
        for ticketIdx, ticket in enumerate(tickets):
            if visited[ticketIdx]: continue
            if ticket[0] != current: continue
            
            copiedVisited = deepcopy(visited)
            copiedRoute = deepcopy(route)
            
            copiedVisited[ticketIdx] = True
            copiedRoute.append(tickets[ticketIdx][1])
            
            stack.append([tickets[ticketIdx][1], copiedVisited, copiedRoute])
    
    return answer