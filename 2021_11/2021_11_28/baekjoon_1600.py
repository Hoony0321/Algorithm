#baekjoon_1600_말이 되고픈 원숭이
#BFS 사용

#=== import module ===#
#=== Function define ===#

def BFS(K,W,H):
  #global matrix,dx,dy,kx,ky;

  queue = [[0,0,K,0]];
  Visited = [[[-1] * W for _ in range(H)] for _ in range(K+1)];
  Visited[K][0][0] = 1;
  min_move = -1;
  while(queue):
    peek = queue.pop(0);
    y = peek[0]; x = peek[1]; k = peek[2]; move = peek[3];

    if y == H-1 and x == W-1: #도착지 도착
      min_move = move;
      break;

    #말처럼 이동하는 경우 (K 횟수 사용)
    if k > 0:
      for i in range(8):
        nextY = y + ky[i]; nextX = x + kx[i];
        if 0 <= nextY < H and 0 <= nextX < W: #범위 안 통과
          if matrix[nextY][nextX] == 1: continue;
          if Visited[k-1][nextY][nextX] == 1: continue;
          Visited[k-1][nextY][nextX] = 1;
          queue.append([nextY,nextX,k-1,move+1]); 
  
    #상하좌우 이동하는 경우 (K 횟수 사용 안 함)
    for i in range(4):
      nextY = y + dy[i]; nextX = x + dx[i];
      if 0 <= nextY < H and 0 <= nextX < W: #범위 안 통과
          if matrix[nextY][nextX] == 1: continue;
          if Visited[k][nextY][nextX] == 1: continue;
          Visited[k][nextY][nextX] = 1;
          queue.append([nextY,nextX,k,move+1]); 
  
  return min_move;

    



#=== variable declare ===#
K = 0; W = 0; H = 0; matrix = [];

dy = [1,0,0,-1]; dx = [0,1,-1,0]; #아래 오른쪽 왼쪽 위
ky = [1, 2, -2, -1, 2, 1, -1, -2]; kx = [2, 1, 1, 2, -1, -2, -2, -1];
#=== main function ===#
K = int(input());
W,H = map(int,input().split());

for _ in range(H):
  matrix.append(list(map(int,input().split())));

print(BFS(K,W,H));