#baekjoon_1325_효율적인 해킹

#=== import module ===#
from collections import deque
import sys

input = sys.stdin.readline
#=== variable declare ===#
answer = []; max_hacking = -1;
#=== Function define ===#
def BFS(startPC, N):
  hackingPC = 0;

  q = deque();
  q.append(startPC);
  visited = [False for _ in range(N+1)];
  visited[startPC] = True;
  while q:
    curPC = q.popleft();
    hackingPC += 1;

    for nextPC in graph[curPC]:
      if visited[nextPC]: continue;
      visited[nextPC] = True;
      q.append(nextPC);

  return hackingPC
#=== main function ===#
N,M = map(int,input().split());

graph = [[] for _ in range(N+1)];

for _ in range(M):
  toPC, fromPC = map(int,input().split());
  graph[fromPC].append(toPC);


for i in range(1,N+1):
  result = BFS(i,N);
  if result > max_hacking:
    max_hacking = result;
    answer = [];
    answer.append(i);
  elif result == max_hacking:
    answer.append(i);

answer.sort();
for elem in answer:
  print(elem, end=' ');
print();