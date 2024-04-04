from collections import deque

def checkRule(y,x, place, visited):
    queue = deque()
    queue.append([y,x])
    visited[y][x] = True
    
    step = 0
    dxy = [[-1,0],[1,0],[0,1],[0,-1]]
    while queue and step != 2:
        for _ in range(len(queue)):
            y,x = queue.popleft()
            for i in range(4):
                ny = y + dxy[i][0]
                nx = x + dxy[i][1]
                
                if not (0 <= ny < len(place)) or not (0 <= nx < len(place[0])):
                    continue
                if place[ny][nx] == 'X':
                    continue
                if visited[ny][nx]:
                    continue
                if place[ny][nx] == 'P':
                    print("BOOM HERE", ny, nx)
                    
                    return False
                
                visited[ny][nx] = True
                queue.append([ny,nx])
        step += 1

    return True

def isValidRoom(place):
    visited= [[False for _ in range(len(place[0]))] for _ in range(len(place))]
    for i in range(len(place)):
        for j in range(len(place[0])):
            if place[i][j] == 'P':
                if(not checkRule(i,j,place, visited)): return 0
    
    print("VISITED RESULT")
    for row in visited:
        print(row)

    return 1

def solution(places):
    answer = []
    
    for place in places:
        answer.append(1 if isValidRoom(place) else 0)
    
    return answer