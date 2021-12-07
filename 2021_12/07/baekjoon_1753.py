#baekjoon_1753_최소경로

#=== import module ===#
import heapq
import sys

input = sys.stdin.readline;
#=== variable declare ===#
V = 0; E = 0; W = []; Dist = [];
#=== Function define ===#
def Dijkstra():
  q = [];
  heapq.heappush(q,(0,start_vertex));
  Dist[start_vertex] = 0;
  while q:
    curWeight, curVertex  = heapq.heappop(q);

    #if Dist[curVertex] < curWeight: continue; 이것도 되고 아랫 것도 됨.
    if Visited[curVertex] : continue;
    Visited[curVertex] = True;

    for info in W[curVertex]:
      vertex = info[0]; cost = info[1];
      if cost + curWeight < Dist[vertex]:
        Dist[vertex] = cost + curWeight;
        heapq.heappush(q,(cost + curWeight,vertex));


#=== main function ===#
V,E = map(int,input().split());
start_vertex = int(input());

W = [[] for _ in range(V+1)];
Dist = [float('INF') for _ in range(V+1)];
Visited = [False for _ in range(V+1)];
for _ in range(E):
  V1, V2, Cost = map(int,input().split());
  W[V1].append((V2,Cost));

Dijkstra();

for i in range(1,V+1):
    print("INF" if Dist[i] == float('INF') else Dist[i]);