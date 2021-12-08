#baekjoon_10282_해킹

#=== import module ===#
import sys
import heapq

input = sys.stdin.readline;
#=== variable declare ===#

#=== Function define ===#
def Dijkstra(N,graph,C):
  result = [0,0]; #감염된 컴퓨터 수, 최소 코스트
  q = [];
  heapq.heappush(q,(0,C));
  weights = [float('INF') for _ in range(N+1) ];
  weights[C] = 0;
  Visited = [False for _ in range(N+1)];
  while q:
    cost, curComputer = heapq.heappop(q);
    #print(curComputer);
    if Visited[curComputer]: continue; #이미 방문한 곳
    Visited[curComputer] = True;
    result[0] += 1;
    if result[1] < weights[curComputer]:
      result[1] = weights[curComputer];

    for info in graph[curComputer]:
      nextPC = info[0]; addCost = info[1];
      if weights[nextPC] > cost + addCost:
        weights[nextPC] = cost + addCost;
        heapq.heappush(q,(cost + addCost, nextPC));
  
  return result;

    

#=== main function ===#
T = int(input());

for _ in range(T):
  N,D,C = map(int,input().split());
  graph = [[] for _ in range(N+1)];
  for _ in range(D):
    toPC, fromPC, cost = map(int,input().split());
    graph[fromPC].append((toPC, cost));
  result = Dijkstra(N,graph,C);
  for elem in result:
    print(elem, end= ' ');
  print();
