#baekjoon_2167_미로탐색

#=== import module ===#

#=== Function define ===#
class Point:
  def __init__(self,y,x):
    self.y = y;
    self.x = x;


def BFS():
  global mapVal,visited,values,row,col;
  #상하좌우
  dx = [0,0,-1,1]; dy = [-1,1,0,0];
  queue = [Point(0,0)];

  while queue:
    peek = queue.pop(0);

    for i in range(4):
      next_x = peek.x + dx[i];
      next_y = peek.y + dy[i];

      if 0 <= next_x < col and 0 <= next_y < row: #범위 체크
        if mapVal[next_y][next_x] == 1 and not visited[next_y][next_x]: #이동 가능
          visited[next_y][next_x] = True;
          values[next_y][next_x] = values[peek.y][peek.x] + 1;
          queue.append(Point(next_y,next_x));
      
      if next_y == row -1 and next_x == col -1:
        queue = [];
  
  print(values[row-1][col-1]);
          

#=== variable declare ===#
row = 0; col = 0;
mapVal = []; visited = []; values = [];
#=== main function ===#
row,col = map(int, input().split());
visited = [[False for _ in range(col)] for _ in range(row)];
values = [[1 for _ in range(col)] for _ in range(row)];

for _ in range(row):
  mapVal.append(list(map(int,list(input()))));

BFS();