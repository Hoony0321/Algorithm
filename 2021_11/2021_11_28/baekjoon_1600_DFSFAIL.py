#baekjoon_1600_말이 되고픈 원숭이 
#DFS 시간초과 -> DP 사용해도 시간초과
#최소거리 찾는 거 -> BFS 사용

#=== import module ===#
import copy
#=== Function define ===#
class Point:
  def __init__(self,y,x):
    self.y = y;
    self.x = x;

def DFS(y,x,k,Visited):

  global matrix,W,H,dx,dy,kdy,kdx,INF,dp;

  if y == H-1 and x == W-1: #도착지 도착
    return 1;

  if dp[k][y][x] != None: #dp값 존재
    return dp[k][y][x];
  
  tmpVisited = copy.deepcopy(Visited);

  min_move = INF;
  #말처럼 이동하는 경우 (K 횟수 사용)
  if k > 0:
    for i in range(8):
      nextY = y + kdy[i]; nextX = x + kdx[i];
      if 0 <= nextY < H and 0 <= nextX < W: #범위 안 통과
        if matrix[nextY][nextX] == 1: continue;
        if tmpVisited[nextY][nextX] : continue;
        tmpVisited[nextY][nextX] = True;
        min_move = min(min_move, DFS(nextY,nextX,k-1,tmpVisited) + 1);
        tmpVisited[nextY][nextX] = False;
  
  #상하좌우 이동하는 경우 (K 횟수 사용 안 함)
  for i in range(4):
    nextY = y + dy[i]; nextX = x + dx[i];
    if 0 <= nextY < H and 0 <= nextX < W: #범위 안 통과
        if matrix[nextY][nextX] == 1: continue;
        if tmpVisited[nextY][nextX] : continue;
        tmpVisited[nextY][nextX] = True;
        min_move = min(min_move, DFS(nextY,nextX,k,tmpVisited) + 1);
        tmpVisited[nextY][nextX] = False;
  
  dp[k][y][x] = min_move;
  return min_move;

#=== variable declare ===#
K = 0; W = 0; H = 0; matrix = [];
Visited = []; INF = float('INF'); dp = [];
#상하좌우 이동
dy = [-1,1,0,0]; dx = [0,0,-1,1];
#말처럼 이동
kdy = [-1,-2,-2,-1,1,2,2,1]; kdx = [-2,-1,1,2,2,1,-1,-2];
#=== main function ===#
K = int(input());
W,H = map(int,input().split());
Visited = [ [False for i in range(W)] for j in range(H)];
for _ in range(H):
  matrix.append(list(map(int,input().split())));
dp = [ [[None for i in range(W)] for p in range(H)]  for j in range(K+1)]

result = DFS(0,0,K,Visited);

if result == float('INF'):
  print(-1);
else:
  print(result-1);


