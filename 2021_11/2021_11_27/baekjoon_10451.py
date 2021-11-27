#baekjoon_10451_순열 사이클

#=== import module ===#

#=== Function define ===#
# def DFS(current, start):
#   global cycle, S;
#   if current == start: #cycle임
#     cycle  += 1; return;
#   else:
#     if Visited[current]: #이미 방문한 곳임.
#       return;
#     else:
#       Visited[current] = True;
#     nextPoint = S[current];
#     DFS(nextPoint,start);

def BFS(idx):
  global Visited,S,cycle;
  queue = [idx];
  cycleList = [idx];

  while(queue):
    peek = queue.pop(0);
    next = S[peek];

    if Visited[next]: continue;
    else:
      Visited[next] = True;
      queue.append(next);
      cycleList.append(next);
  
  if cycleList[0] == cycleList[-1]:
    cycle += 1;

  
  

#=== variable declare ===#
T = 0; N = 0; S = []; Visited = []; cycle = 0;
#=== main function ===#
T = int(input());

for _ in range(T):
  N = int(input());
  S = list(map(int,input().split()));
  for i in range(N):
    S[i] = S[i] - 1;
    
  Visited = [False for i in range(N)];
  cycle = 0;
  for i in range(N):
    if Visited[i]: #이미 방문한 곳
      continue;
    
    #새로 방문
    BFS(i);
  
  print(cycle);