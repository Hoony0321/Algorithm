#baekjoon_2573_빙산

#=== import module ===#
from collections import deque
#=== variable declare ===#
matrix = []; dy = [-1,1,0,0]; dx = [0,0,1,-1]; years = 0;
#=== Function define ===#
def ReturningDistrict(Pos,visited,R,C):
  if visited[Pos[0]][Pos[1]]: return;
  if matrix[Pos[0]][Pos[1]] == 0:
    visited[Pos[0]][Pos[1]] = True; return False;

  queue = deque();
  queue.append(Pos);

  while queue:
    item = queue.popleft(); y = item[0]; x = item[1];
    if visited[y][x] : continue;
    visited[y][x] = True;

    for p in range(4):
      ny = y + dy[p]; nx = x + dx[p];
      if matrix[ny][nx] == 0: continue;
      if visited[ny][nx]: continue;
      queue.append([ny,nx]);
  
  return True;

def MeltingIce(R,C):
  tmpMat = [[0 for _ in range(C)] for _ in range(R)];
  for y in range(1,R):
    for x in range(1,C):
      if matrix[y][x] == 0: continue;
      count = 0;
      for p in range(4):
        ny = y + dy[p]; nx = x + dx[p];
        if matrix[ny][nx] == 0: count += 1;
        tmpMat[y][x] = count;
  
  for y in range(1,R):
    for x in range(1,C):
      if tmpMat[y][x] != 0:
        matrix[y][x] -= tmpMat[y][x];
        if matrix[y][x] < 0 : matrix[y][x] = 0;
      
      





def solve(R,C):
  global years;
  while(1):
    #몇덩어리인지 확인
    visited = [[False for _ in range(C)] for _ in range(R)];
    districts = 0;
    for i in range(1,R):
      for j in range(1,C):
        if ReturningDistrict([i,j],visited,R,C): districts += 1;
    
    if districts > 1: return years;
    elif districts == 0: return 0;

    #빙산 녹이기
    MeltingIce(R,C);
    years += 1;

  
  print(districts);
#=== main function ===#
R,C = map(int,input().split());
for _ in range(R):
  matrix.append(list(map(int,input().split())));

print(solve(R,C));
