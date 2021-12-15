#baekjoon_1504_특정한 최단 경로

#=== import module ===#
import heapq
import sys

input= sys.stdin.readline
#=== variable declare ===#

#=== Function define ===#
def MST(fromV,toV,N,E):
  dist = [float('INF') for _ in range(N+1)]; dist[fromV] = 0;
  visited = [False for _ in range(N+1)];
  queue = [];
  heapq.heappush(queue,(0,fromV)); #현재까지 비용, 현 지점

  while queue:
    curCost, curVertex = heapq.heappop(queue);

    if curVertex == toV: break;

    if visited[curVertex]: continue; #이미 방문한 지점
    visited[curVertex] = True;
    for vertex, cost in info[curVertex]:
      if dist[vertex] > curCost + cost:
        heapq.heappush(queue,(curCost + cost, vertex));
        dist[vertex] = curCost + cost;
  
  return dist[toV];
  


#=== main function ===#
N, E = map(int,input().split());
info = [[] for _ in range(N+1)];

for _ in range(E):
  vertex1, vertex2, cost = map(int,input().split());
  info[vertex1].append((vertex2,cost));
  info[vertex2].append((vertex1,cost));

target1, target2 = map(int,input().split());

# target1 거치고 target2 가는 방법
cost1 = MST(1,target1,N,E) + MST(target1,target2,N,E) + MST(target2,N,N,E);
cost2 = MST(1,target2,N,E) + MST(target2,target1,N,E) + MST(target1,N,N,E);

min_cost = min(cost1,cost2);
if min_cost == float('INF'): print(-1);
else: print(min_cost);