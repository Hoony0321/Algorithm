from collections import deque

def solution(maps):
    MAX_ROW = len(maps)
    MAX_COL = len(maps[0])
    VISITED = [[False] * MAX_COL for _ in range(MAX_ROW)]
    
    dxy = [[0,1], [0,-1], [1,0], [-1,0]]
    queue = deque([[0,0]])
    count = 0
            
    
    while(queue):
        count += 1
        for _ in range(len(queue)): # one cycle
            y,x = queue.popleft()

            if(VISITED[y][x]): continue
            VISITED[y][x] = True
            
            if(y == MAX_ROW - 1 and x == MAX_COL - 1): # 목적지 도착
                return count
            
            for dy,dx in dxy:
                ny,nx = y + dy, x + dx
                if(0 <= ny < MAX_ROW and 0 <= nx < MAX_COL):
                    if(maps[ny][nx] == 0): continue
                    queue.append([ny,nx])
        
    return -1