from collections import deque

dx = [0,0,1,-1]
dy = [1,-1,0,0]

def findShortestPath(startPos, targetPos, maps):
    moveCount = 0
    
    visited = [[False] * len(maps[0]) for _ in range(len(maps))]
    
    queue = deque()
    queue.append(startPos)
    visited[startPos[0]][startPos[1]] = True
    
    isArrived = False
    
    while (queue and not isArrived):
        size = len(queue)
        for _ in range(size):
            y,x = queue.popleft()

            for i in range(4):
                ny, nx = y + dy[i], x + dx[i]

                if(ny < 0 or ny >= len(maps) or nx < 0 or nx >= len(maps[0])):
                    continue
                if(maps[ny][nx] == 'X'): continue
                if(visited[ny][nx]): continue
                visited[ny][nx] = True
                
                if(ny == targetPos[0] and nx == targetPos[1]):
                    isArrived = True
                    break
                
                queue.append([ny,nx])
    
            if(isArrived): break
                
        moveCount += 1
    
    return moveCount if isArrived else -1
    

def solution(maps):
    startPos = [0,0]
    endPos = [0,0]
    leverPos = [0,0]
    
    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if maps[i][j] == 'S':
                startPos = [i,j]
            elif maps[i][j] == 'E':
                endPos = [i,j]
            elif maps[i][j] == 'L':
                leverPos = [i,j]

    
    moveCount1 = findShortestPath(startPos, leverPos, maps)
    if(moveCount1 == -1): return -1

    moveCount2 = findShortestPath(leverPos, endPos, maps)
    if(moveCount2 == -1): return -1 
    
    return moveCount1 + moveCount2