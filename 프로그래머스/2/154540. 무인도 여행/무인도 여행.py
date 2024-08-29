from collections import deque
def solution(maps):
    answer = []
    visited = [[False for _ in range(len(maps[0]))] for _ in range(len(maps))]
    
    queue = deque()
    dxy = [[0,1],[0,-1],[1,0],[-1,0]]
    
    for i in range(0,len(maps)):
        for j in range(0,len(maps[0])):
            if visited[i][j]: continue
            visited[i][j] = True
            if visited[i][j] == 'X': continue
            
            queue.append([i,j])
            islandSize = 0
            while queue:
                cy,cx = queue.pop()
                if maps[cy][cx] == 'X': continue
                islandSize += int(maps[cy][cx])
                
                for dy,dx in dxy:
                    ny = cy + dy
                    nx = cx + dx
                    
                    if ny < 0 or nx < 0 or ny >= len(maps) or nx >= len(maps[0]): continue
                    if visited[ny][nx]: continue
                    visited[ny][nx] = True
                    
                    queue.append([ny,nx])
            if islandSize != 0:    
                answer.append(islandSize)
    answer.sort()
    
    return answer if answer else [-1]