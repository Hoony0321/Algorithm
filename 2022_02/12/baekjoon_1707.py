#baekjoon_1707_이분그래프
#bind 'set enable-bracketed-paste off'

#=== import module ===#
from collections import deque
import re
#=== variable declare ===#
graphInfo = []; visited = [];
RED = 1; BLUE = 2;
#=== Function define ===#
def PaintColor(start):
  queue = deque();
  queue.append(start);
  color[start] = RED; #첫번째 시작 노드 색깔은 RED로 통일
  isAvailable = True;
  while queue:
    curVertex = queue.popleft();
    if color[curVertex] == RED:
      nextColor = BLUE;
    else:
      nextColor = RED;
    
    for nextVertex in graphInfo[curVertex]:
      if color[nextVertex] == nextColor: continue; #이미 queue에 들어가있음. or 이미 방문함.
      elif color[nextVertex] == -1: #첫 방문임.
        color[nextVertex] = nextColor;
        queue.append(nextVertex);
      else: #첫 방문도 아니고 색깔도 다름. 존재 불가
        isAvailable = False;
        queue = [];
        break;
  
  return isAvailable;


  



#=== main function ===#

K = int(input());

for _ in range(K):
  V,E = map(int,input().split());
  graphInfo = [[] for _ in range(V+1)];
  
  for _ in range(E): #간선 정보 입력
    V1, V2 = map(int,input().split());
    graphInfo[V1].append(V2);
    graphInfo[V2].append(V1);
  
  color = [-1 for _ in range(V+1)]; # -1: 무색 1: 파랑 2: 빨강
  
  isAvailable = True;
  for vertex in range(1,V+1):
    if color[vertex] == -1:
      isAvailable = PaintColor(vertex);
    if not isAvailable: break;
  
  if isAvailable: print("YES");
  else: print("NO");