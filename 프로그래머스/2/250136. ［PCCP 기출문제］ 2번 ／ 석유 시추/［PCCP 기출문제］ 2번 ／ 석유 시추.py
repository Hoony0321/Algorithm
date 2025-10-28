from collections import deque

def solution(land):
    n = len(land)
    m = len(land[0])
    visited = [[False for _ in range(m)] for _ in range(n)]
    dxy = [[0,1],[1,0],[0,-1],[-1,0]]
    group_size = [0,0]
    group_num = 1
    
    for i in range(n):
        for j in range(m):
            if land[i][j] == 0: continue
            if visited[i][j]: continue
            visited[i][j] = True
            group_num += 1
            group_size.append(0)
            
            # dfs
            stack = deque()
            stack.append([i,j])
            while stack:
                y,x = stack.pop()
                group_size[group_num] += 1
                land[y][x] = group_num
                
                for dy,dx in dxy:
                    ny = y + dy
                    nx = x + dx
            
                    if ny < 0 or nx < 0 or ny >= n or nx >= m: continue
                    if land[ny][nx] == 0: continue
                    if visited[ny][nx]: continue
                    visited[ny][nx] = True
                    stack.append([ny,nx])
    
    print(group_size)
    
    max_oil = 0
    for i in range(m):
        oil = 0
        group_set = set()
        for j in range(n):
            if land[j][i] != 0:
                group_set.add(land[j][i])
        
        for num in group_set:
            oil += group_size[num]
        
        max_oil = max(max_oil, oil)
            
    
    return max_oil