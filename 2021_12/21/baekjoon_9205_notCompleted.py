#baekjoon_9205_맥주 마시면서 걸어가기

#1. 현위치에서 맥주 20병을 가진 채로 출발한다.
#2. 1000M 초과하기 전에 페스티벌 or 편의점에 도착해야 한다.
#3. 도착 못 할 경우는 실패, 페스티벌에 도착할 경우 성공 or 편의점에 도착할 경우 다시 1번으로 돌아감.


#=== import module ===#
from collections import deque
#=== variable declare ===#

#=== Function define ===#
def BFS(store):
  queue = deque();
  queue.append([startPos[0], startPos[1], 0]); # x,y, visited
  arrival = False;
  while queue:
    x,y,visited = queue.popleft();
    
    
    for i in range(store):
      if visited & (1 << i) != 0 : continue; #이미 방문한 곳
      nx = storePos[i][0]; ny = storePos[i][1]; #다음 좌표
      if (abs(nx - x) + abs(ny - y)) > 1000: continue; #해당 편의점까지 못 감.
      if (abs(dest[0] - nx) + abs(dest[1]- ny)) <= 1000: 
        arrival = True; break; #목적지 도착 가능
      
      
      #목적지 도착 불가 -> 다음 편의점으로 이동
      queue.append([nx,ny,visited | (1 << i)]);
    
    if arrival: break;
  
  return arrival;
      


    
    
    


#=== main function ===#
T = int(input());

for _ in range(T):
  store = int(input()); #편의점 개수
  startPos = list(map(int,input().split())); #현 위치
  storePos = [];
  for _ in range(store):
    storePos.append(list(map(int,input().split())));
  
  dest = list(map(int,input().split()));

  if (abs(dest[0] - startPos[0]) + abs(dest[1] - startPos[1])) <= 1000:
    print('happy'); continue;

  if BFS(store): print('happy');
  else: print('sad');
