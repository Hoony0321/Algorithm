from collections import deque

def solution(maps):
    MAX_ROW = len(maps)
    MAX_COL = len(maps[0])
    dxy = [[-1,0],[1,0],[0,-1],[0,1]]
    visited = [[False for _ in range(MAX_COL)] for _ in range(MAX_ROW)]
    queue = deque()
    
    queue.append([0,0])
    visited[0][0] = True
    
    isFind = False
    count = 1
    while (queue and not isFind):
        count += 1
        queueSize = len(queue)
        
        for _ in range(queueSize):
            if(isFind): break
            y,x = queue.popleft()

            for dy,dx in dxy:
                ny,nx = y + dy, x + dx

                if ny < 0 or ny >= MAX_ROW or nx < 0 or nx >= MAX_COL: continue
                if maps[ny][nx] == 0: continue
                if visited[ny][nx]: continue
                
                if(ny == MAX_ROW-1 and nx == MAX_COL-1):
                    queue.clear()
                    isFind = True
                    break

                queue.append([ny,nx])
                visited[ny][nx] = True
    
    return count if isFind else -1