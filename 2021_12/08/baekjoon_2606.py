#baekjoon_2606_바이러스

#=== import module ===#
import sys
from collections import deque

input = sys.stdin.readline;
#=== variable declare ===#
C = 0; E = 0; graph = [];
#=== Function define ===#
def BFS(C,E):
  q = deque();
  q.append(1);
  virus = 0;
  visited = [False for _ in range(C+1)];
  visited[1] = True;
  while q:
    curPC = q.popleft();
    for nextPC in graph[curPC]:
      if visited[nextPC]: continue;
      visited[nextPC] = True;
      virus += 1;
      q.append(nextPC);

  return virus;



#=== main function ===#
C = int(input()); E = int(input());
graph = [[] for _ in range(C+1)];
for _ in range(E):
  pc1, pc2 = map(int,input().split());
  graph[pc1].append(pc2);
  graph[pc2].append(pc1);

print(BFS(C,E));