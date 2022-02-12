#baekjoon_1707_이분그래프

#=== import module ===#
from collections import deque
import re
#=== variable declare ===#
graphInfo = [];
#=== Function define ===#
def ReturnAdjGraph(start):
  result = [];
  queue = deque();
  queue.append(start);
  visited = [False for _ in range(V+1)];

  while queue:
    curVertex = queue.popleft();
    visited[curVertex] = True;
    result.append(curVertex);

    for nextVertex in range(1,V+1):
      if visited[nextVertex] : continue;
      if graphInfo[curVertex][nextVertex] == 0: continue;
      queue.append(nextVertex);
      
  return result;


#=== main function ===#

K = int(input());

for _ in range(K):
  V,E = map(int,input().split());
  graphInfo = [[0 for _ in range(V+1)] for _ in range(V+1)];
  
  for _ in range(E): #간선 정보 입력
    V1, V2 = map(int,input().split());
    graphInfo[V1][V2] = 1;
    graphInfo[V2][V1] = 1;
  
  graph1 = ReturnAdjGraph(1);
  print(graph1);