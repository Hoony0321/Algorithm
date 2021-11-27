#baekjoon_1600_말이 되고픈 원숭이 
#DFS 시간초과

#=== import module ===#
import copy
#=== Function define ===#
def DFS(y,x,k,move,Visited):

  global matrix, min_move,W,H,dx,dy,kdy,kdx;

  if min_move < move:
    return;

  if y == H-1 and x == W-1: #도착지 도착
    min_move = min(min_move, move);
    return;
  
  if Visited[y][x]: #이미 방문
    return;
  
  
  tmpVisited = copy.deepcopy(Visited);
  tmpVisited[y][x] = True;
  
  if matrix[y][x] == 1: return; #벽임.

  #말처럼 이동하는 경우 (K 횟수 사용)
  if k > 0:
    for i in range(8):
      nextY = y + kdy[i]; nextX = x + kdx[i];
      if 0 <= nextY < H and 0 <= nextX < W: #범위 안 통과
        DFS(nextY,nextX,k-1,move+1,tmpVisited);
  
  #상하좌우 이동하는 경우 (K 횟수 사용 안 함)
  for i in range(4):
    nextY = y + dy[i]; nextX = x + dx[i];
    if 0 <= nextY < H and 0 <= nextX < W: #범위 안 통과
      DFS(nextY,nextX,k,move+1,tmpVisited);

#=== variable declare ===#
K = 0; W = 0; H = 0; matrix = []; min_move = float('INF');
Visited = [];
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

DFS(0,0,K,0,Visited);

if min_move == float('INF'):
  print(-1);
else:
  print(min_move);
