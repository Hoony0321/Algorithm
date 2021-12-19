#baekjoon_5014_스타트링크

#총 F층으로 이루어진 건물, 목표 층 G, 현위치 S층, 위로 U만큼, 아래로 D만큼 이동

#=== import module ===#
from collections import deque
#=== variable declare ===#

#=== Function define ===#
def BFS(F,S,G,I,D):
  queue = deque();
  queue.append(S);
  visited = [False for _ in range(F+1)];
  move = [U,-D];
  action = 0;
  found = False;
  while queue:
    action +=1 ;
    for _ in range(len(queue)):
      curFloor = queue.popleft();
      
      #위, 아래로 이동
      for i in range(2):
        nextFloor = curFloor + move[i];
        if nextFloor <= 0 or nextFloor > F: continue;
        if visited[nextFloor]: continue;
        if nextFloor == G : found = True; break;
        visited[nextFloor]= True;
        queue.append(nextFloor);
      
      if found: return action;
  
  return -1;

    
  




#=== main function ===#
F,S,G,U,D = map(int,input().split());
if S == G: print(0); exit(0);
result = BFS(F,S,G,U,D);
if result == -1: print("use the stairs");
else: print(result);