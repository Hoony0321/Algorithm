#baekjoon_1260_DFS와 BFS

#=== import module ===#

#=== Function define ===#
def DFS(V):
  global Matrix; global N;
  visited = [];
  stack = [V];

  while(stack):
    top = stack.pop();
    visited.append(top);

    #인접한 노드 stack에 추가
    for p in range(N,0,-1):
      if Matrix[top][p] == 1 and p not in visited:
        if p in stack:
          stack.remove(p);
        stack.append(p);
  
  for elem in visited:
    print(elem, end= ' ');



def BFS(V):
  global Matrix; global N;
  visited = [];
  queue = [V];

  while(queue):
    peek = queue.pop(0);
    visited.append(peek);

    #인접한 노드 queue에 추가
    for p in range(1,N+1):
      if Matrix[peek][p] == 1 and p not in visited and p not in queue:
        queue.append(p);
    
  for elem in visited:
    print(elem, end= ' ');

#=== variable declare ===#
N = 0; M = 0; V = 0;

#=== main function ===#
N,M,V = map(int,input().split());

#매트릭스 설정
Matrix = [[0 for i in range(N+1)] for j in range(N+1)];
#간선 설정
for _ in range(M):
  v1,v2 = map(int,input().split());
  Matrix[v1][v2] = 1;
  Matrix[v2][v1] = 1;

DFS(V);
print();
BFS(V);


