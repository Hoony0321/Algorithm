#baekjoon_2468_안전영역

#=== import module ===#
import copy
#=== Function define ===#
class Point:
  def __init__(self,y,x):
    self.y = y;
    self.x = x;

def Flooding(mapVal,height):
  global N;

  for i in range(N):
    for j in range(N):
      if mapVal[i][j] <= height:
        mapVal[i][j] = -1;

def BFS(mapVal, visited):
  global safeArea;
  #상하좌우
  dy = [-1,1,0,0]; dx = [0,0,-1,1]; 

  for i in range(N):
    for j in range(N):
      if not visited[i][j]:
        visited[i][j] = True;
        if mapVal[i][j] == -1: continue;

        queue = [Point(i,j)];
        safeArea[-1] += 1;
        print(queue[0].y, queue[0].x);
        while(queue):
          peek = queue.pop(0);

          for i in range(4):
            nextY = peek.y + dy[i]; nextX = peek.x + dx[i];
            if 0 <= nextX < N and 0 <= nextY < N:
              if not visited[nextY][nextX]: #방문 안 함
                visited[nextY][nextX] = True;
                if mapVal[nextY][nextX] != -1:
                  queue.append(Point(nextY,nextX));

  


  
  

def FindSafeArea(height):
  global N,originMap,safeArea;
  mapVal = copy.deepcopy(originMap);
  visited = [[False for _ in range(N)] for _ in range(N)];
  isNew = True;
  
  #해당 지점까지 물에 잠구기
  Flooding(mapVal,height);

  for row in mapVal:
    for elem in row:
      print(elem, end=' ');
    print();

  BFS(mapVal,visited);
  
  
  


#=== variable declare ===#
N = 0; originMap = []; maxH = 1; minH = 100;
result = []; safeArea = [];
#=== main function ===#
N = int(input());

for _ in range(N):
  originMap.append(list(map(int,input().split())));

#minH,maxH 찾기
for row in originMap:
  for height in row:
    if height < minH: minH = height;
    if height > maxH: maxH = height;

for height in range(minH,maxH):
  safeArea.append(0);
  FindSafeArea(height);
  print("here");

print(safeArea);


