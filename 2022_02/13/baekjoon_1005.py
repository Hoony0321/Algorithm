#baekjoon_1005_ACM Craft

#=== import module ===#
from collections import deque
#=== variable declare ===#
D = []; #건설 시간 배열
constructionOrder = []; #건설 순서 배열
#=== Function define ===#
def ReturnShortestTime():
  global N,K,W;
  queue = deque();
  for orderNum in range(1,N+1):
    if len(constructionOrder[orderNum]) == 0: #선행되는 건설이 없는 경우 -> 첫번째 노드 시작
      queue.append(orderNum);
  
  while queue:
    buildingNum = queue.popleft();
    if buildingNum == W:
      break;

    for orderNum in range(1,N+1):
      if orderNum == buildingNum: continue; #자기 자신
      if buildingNum in constructionOrder[orderNum]: 
        constructionOrder[orderNum].remove(buildingNum);
        D[orderNum].append(D[buildingNum][0]);
        if len(constructionOrder[orderNum]) == 0: #선행되는 건물 없음 이제.
          queue.append(orderNum);
          D[orderNum][0] += max(D[orderNum][1:]);

  
  return D[W][0];
#=== main function ===#
T = int(input()); #테스트케이스

for _ in range(T):
  N,K = map(int,input().split()); #건물 수, 규칙 수
  D = [[t] for t in list(map(int,input().split()))];
  D = [[]] + D;
  constructionOrder = [[] for _ in range(N+1)];
  for _ in range(K):
    pre, next = map(int,input().split());
    constructionOrder[next].append(pre);
  
  W = int(input());
  
  resultTime = ReturnShortestTime();
  print(resultTime);

