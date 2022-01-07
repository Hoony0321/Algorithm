#baekjoon_13460_구슬 탈출 2

#=== import module ===#
from collections import deque
#=== variable declare ===#
N = -1; #세로 길이
M = -1; #가로 길이
board = []; #맵 행렬
nxy = [[0,-1],[0,1],[1,0],[-1,0]]
FirstPos = [None for _ in range(2)]; #빨간 공 파란 공 첫 위치 배열
#=== Function define ===#
def BFS(N,M):
  visited = [[False for _ in range(N * M)] for _ in range(N * M)];
  queue = deque();
  queue.append(FirstPos);
  action = 0;
  success = False;
  while queue:
    if action == 10: break;

    for _ in range(len(queue)):
      curRed, curBlue = queue.popleft();

      for delta in nxy:
        available = True;
        hole = [False,False]; move = [0,0];
        nextRedY = curRed[0]; nextRedX = curRed[1]; nextBlueY = curBlue[0]; nextBlueX = curBlue[1];
        while(1): #Red 공 진행
          nextRedY += delta[0]; nextRedX += delta[1];
          if board[nextRedY][nextRedX] == '#': #더이상 진행하지 못 함.
            nextRedY -= delta[0]; nextRedX -= delta[1];
            break;
          
          if board[nextRedY][nextRedX] == 'O': #구멍에 빠짐.
            hole[0] = True;
            break;
          move[0] += 1;
        while(1): #Blue 공 진행
          nextBlueY += delta[0]; nextBlueX += delta[1];
          if board[nextBlueY][nextBlueX] == '#': #더이상 진행하지 못 함.
            nextBlueY -= delta[0]; nextBlueX -= delta[1];
            break;
          
          if board[nextBlueY][nextBlueX] == 'O': #구멍에 빠짐.
            hole[1] = True;
            break;
          
          move[1] += 1;
        
        if hole[1] == True: #성립하지 않는 경우 -> 넘어감
          continue;
        elif hole[0] == True: #성공 조건
          success = True; break;
        
        if nextRedY == nextBlueY and nextRedX == nextBlueX: #둘이 같은 곳에 있음. 늦게 온 쪽을 한 발 뒤로
          if move[0] > move[1]: #Red가 더 늦게 옴.
            nextRedY -= delta[0]; nextRedX -= delta[1];
          else: #Blue가 더 늦게옴.
            nextBlueY -= delta[0]; nextBlueX -= delta[1];
        
        if visited[nextRedY * M + nextRedX][nextBlueY * M + nextBlueX] == True: #이미 방문한 곳.->넘어감
          continue; 
        visited[nextRedY * M + nextRedX][nextBlueY * M + nextBlueX] = True;
        queue.append([[nextRedY,nextRedX],[nextBlueY,nextBlueX]]);
        

    action += 1;  
    if success: break;
  
  if not success: return -1;
  else: return action;
    



#=== main function ===#
N, M = map(int,input().split());

for i in range(N):
  row = list(input());
  for j in range(M):
    if row[j] == 'R':
      FirstPos[0] = [i,j];
      row[j] = '.';
    elif row[j] == 'B':
      FirstPos[1] = [i,j];
      row[j] = '.';
  board.append(row);

print(BFS(N,M));