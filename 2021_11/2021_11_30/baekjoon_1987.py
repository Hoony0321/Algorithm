#baekjoon_1987_알파벳

#=== import module ===#
from copy import deepcopy
#=== Function define ===#
def DFS(y,x,visited,count):
  global max_move;

  if count > max_move:
    max_move = count;

  for i in range(4):
    nextY = y + dy[i]; nextX = x + dx[i];
    if 0 <= nextY < R and 0 <= nextX < C: #범위 통과
      nextChar = ord(board[nextY][nextX]) - 65;
      if visited[nextChar]: continue; #이미 방문한 곳임.
      visited[nextChar] = True;
      DFS(nextY,nextX,visited,count +1);
      visited[nextChar] = False;





#=== variable declare ===#
R = 0; C = 0; board = []; recordBoard = []; visited = [];
dx = [-1,1,0,0]; dy = [0,0,-1,1]; max_move = 0;
#=== main function ===#
R,C = map(int,input().split());
board = [[""] * C for _ in range(R)];
visited = [False for i in range(26)];


for i in range(R):
  inputStr = input();
  for j in range(C):
    board[i][j] = inputStr[j];

visited[ord(board[0][0]) - 65] = True;
DFS(0,0,visited,1);
print(max_move);