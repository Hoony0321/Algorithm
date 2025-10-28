from collections import deque

def solution(land):
    n = len(land)
    m = len(land[0])
    visited = [[False] * m for _ in range(n)]
    dxy = [[0,1],[1,0],[0,-1],[-1,0]]
    oils = [0] * m
    
    def dfs(y,x):
        stack = deque()
        stack.append([y,x])
        visited[y][x] = True
        oil = 0
        w_set = set()
        
        while stack:
            y,x = stack.pop()
            w_set.add(x)
            oil += 1
            
            
            for dy,dx in dxy:
                ny = y + dy
                nx = x + dx
                
                if ny < 0 or nx < 0 or ny >= n or nx >= m: continue
                if land[ny][nx] == 0: continue
                if visited[ny][nx]: continue
                
                visited[ny][nx] = True
                stack.append([ny,nx])
        
        for w in w_set:
            oils[w] += oil
            
            
    for i in range(n):
        for j in range(m):
            if land[i][j] == 0: continue
            if visited[i][j]: continue
            dfs(i,j)
            
    return max(oils)