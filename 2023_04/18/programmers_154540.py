#문제정보
#programmers_154540 - 무인도 영행 (난이도 2)

from collections import deque 

def solution(maps):
    answer = []
    MAX_R, MAX_C = len(maps), len(maps[0])
    visited = [[False] * MAX_C for _ in range(MAX_R)]
    nxy = [[-1,0], [1,0], [0,1], [0,-1]] #상하좌우
        
    
    def dfs(y,x):
        stack = deque([])
        stack.appendleft([y,x])
        islandSize = 0
        
        while stack:
            curY, curX = stack.popleft()
            if(visited[curY][curX]): continue #이미 방문한 경우
            print(f"Y : {curY}  X : {curX}")
            visited[curY][curX] = True #아직 방문하지 않은 경우
            
            if(maps[curY][curX] == 'X'): continue #섬이 아닌 경우 -> 탈출
            islandSize += int(maps[curY][curX]) #맵 사이즈에 추가
            
            for dy,dx in nxy:
                ny, nx = curY + dy, curX + dx
                if(not(0 <= nx <= MAX_C-1)): continue
                if(not(0 <= ny <= MAX_R-1)): continue
                if(visited[ny][nx]): continue
                stack.appendleft([ny,nx])
        
        return islandSize
    
    for i in range(MAX_R):
        for j in range(MAX_C):
            islandSize = dfs(i, j)
            
            if islandSize != 0: 
                answer.append(islandSize)
        
    if(len(answer) == 0): answer.append(-1)    
    answer.sort()
    return answer