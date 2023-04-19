#문제정보
#programmers_1844 - 게임 맵 최단거리 (난이도 2)

from collections import deque

def solution(maps):
    MAX_ROW = len(maps)
    MAX_COL = len(maps[0])
    dxy = [[-1,0],[1,0],[0,-1],[0,1]]

    visited = [[False] * MAX_COL for _ in range(MAX_ROW)]
    
    queue = deque([[0,0]])
    count = 0
    find = False
    while queue and not find:
        for _ in range(len(queue)): #한 사이클
            y, x = queue.popleft()
        
            if(visited[y][x]): continue #이미 방문함
            else: visited[y][x] = True #처음 방문함
            
            if(maps[y][x] == 0): continue #벽이 있는 자리
            
            if(y == MAX_ROW-1 and x == MAX_COL-1): #도착
                find = True
                break
            
            for dy,dx in dxy:
                ny,nx = y + dy, x + dx
                if(not(0 <= ny <= MAX_ROW-1)): continue #맵 범위 벗어남
                if(not(0 <= nx <= MAX_COL-1)): continue #맵 범위 벗어남    
                queue.append([ny,nx])
            
        count += 1
            
        
    
        
    
    return count if find else -1