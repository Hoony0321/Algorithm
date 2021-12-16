#baekjoon_14442_벽 부수고 이동하기 2_renew
#좀 더 뺘르게

#=== import module ===#
from collections import deque
import sys
input=sys.stdin.readline
#=== variable declare ===#

#=== Function define ===#
def BFS(N,M,K):
  dist = [[-1 for _ in range(M+1)] for _ in range(N+1)];
  
  queue = deque();
  queue.append((1,1,K));  #curY, curX, curK
  action = 1;
  while queue:
    for _ in range(len(queue)):
      y, x, curK = queue.popleft();

      if y == N and x == M: return action; #종료

      if dist[y][x] >= curK : continue; #이미 방문한 곳

      dist[y][x] = curK;

      for i in range(4):
        nextY = y + dy[i]; nextX = x + dx[i];
        if not (1 <= nextY <= N and 1 <= nextX <= M) : continue; # 맵 범위 벗어남
        #K 미사용 - 길로만 이동
        if matrix[nextY-1][nextX-1] == '0':
          queue.append((nextY,nextX,curK));
        #K 사용 - 벽 부수고 이동
        else:
          if curK > 0:
            queue.append((nextY,nextX,curK - 1));
    action += 1;
  
  return -1;
    



  

#=== main function ===#
N,M,K = map(int,input().split());
matrix = [];
# 우, 하, 좌, 상 이동
dy = [0,1,0,-1] ; dx = [1,0,-1,0];

matrix = [input().rstrip() for _ in range(N)];

print(BFS(N,M,K));

