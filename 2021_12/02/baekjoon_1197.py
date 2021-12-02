#baekjoon_1197_최소 스패닝 트리
#트리 -> 사이클이 없는 그래프
#같은 사이클이 아닌지 아는 법 -> 유니온 방법 사용.
#=== import module ===#
from collections import deque
#=== Function define ===#
def Find(vertex):
  if P[vertex] == vertex:
    return vertex;
  else:
    p = Find(P[vertex]);
    P[vertex] = p;
    return p;


def Union(vertex1, vertex2):
  p1 = Find(vertex1); p2 = Find(vertex2);
  if p1 != p2:
    P[p2] = p1;
 
  

def MST():
  contain_vertex = 0;
  currentIdx = 0;
  totalWeight = 0;

  while(1):
  
    #모든 간선 연결 완료.
    if contain_vertex == V-1: break;

    #간선 정보 꺼내기
    currentEdge = info[currentIdx];
    vertex1 = currentEdge[0]; vertex2 = currentEdge[1]; weight = currentEdge[2];

    if Find(vertex1) != Find(vertex2):
      Union(vertex1,vertex2);
      contain_vertex += 1;
      totalWeight += weight;
    
    #다음 단계로 진행
    currentIdx += 1;
  
  return totalWeight;






#=== variable declare ===#
V = 0; E = 0; info = []; P = [];
#=== main function ===#
V,E = map(int,input().split());
P = [i for i in range(V+1)];

for _ in range(E):
  info.append(list(map(int,input().split())));

info.sort(key=lambda x:x[2]);


print(MST());