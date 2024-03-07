from queue import PriorityQueue
from collections import deque

dxys = [[1,0],[-1,0],[0,1],[0,-1]]

def solution(land, height):
    answer = 0
    visited = [[False] * len(land) for _ in range(len(land))]
    flagQueue = PriorityQueue()
    
    
    y,x = 0,0
    
    while True:
        queue = deque()
        queue.append([y,x])
        
        while queue:
            y,x = queue.pop()
            visited[y][x] = True
            
            for dxy in dxys:
                ny,nx = y + dxy[0], x + dxy[1]
                if(0 > ny or ny >= len(land) or 0 > nx or nx >= len(land)): continue
                if(visited[ny][nx]): continue
                if(abs(land[y][x] - land[ny][nx]) > height):
                    flagQueue.put([abs(land[y][x] - land[ny][nx]), ny, nx])
                    continue
            
                visited[ny][nx] = True
                queue.append([ny,nx])
        
        # 사다리 놓을 자리 찾기
        cost = -1
        while True:
            if(flagQueue.empty()): break
            elem = flagQueue.get()
            if(visited[elem[1]][elem[2]]): continue
            cost,y,x = elem
            break
        
        if(cost == -1): break
        answer += cost
        
    return answer