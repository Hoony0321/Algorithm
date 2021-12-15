#baekjoon_14442_벽 부수고 이동하기 2

#=== import module ===#
from collections import deque
import sys
input=sys.stdin.readline
#=== variable declare ===#

#=== Function define ===#
def BFS(N,M,K):
  dist = [[[float('INF') for _ in range(K+1)] for _ in range(M+1)] for _ in range(N+1)];
  
  queue = deque();
  queue.append((1,1,1,K));  #curPosition, curAction, curK

  while queue:
    y, x, curAction, curK = queue.popleft();

    if dist[y][x][curK] <= curAction: continue;
    for i in range(0,curK+1):
      if dist[y][x][i] > curAction:
        dist[y][x][i] = curAction;

    for i in range(4):
      nextY = y + dy[i]; nextX = x + dx[i];
      if not (1 <= nextY <= N and 1 <= nextX <= M) : continue; # 맵 범위 벗어남
      #K 미사용 - 길로만 이동
      if matrix[nextY-1][nextX-1] == 0:
        queue.append((nextY,nextX,curAction + 1,curK));
      #K 사용 - 벽 부수고 이동
      else:
        if curK > 0:
          queue.append((nextY,nextX,curAction + 1,curK - 1));
  
  return min(dist[N][M]);


  

#=== main function ===#
N,M,K = map(int,input().split());
matrix = [];
# 우, 하, 좌, 상 이동
dy = [0,1,0,-1] ; dx = [1,0,-1,0];
for _ in range(N):
  matrix.append(list(map(int,list(input().rstrip()))));

result = BFS(N,M,K);

if result == float('INF'): print(-1);
else: print(result);
