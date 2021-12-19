#baekjoon_2644_촌수계산

#=== import module ===#
from collections import deque
#=== variable declare ===#
relationInfo = []; parentInfo = [];
#=== Function define ===#
def FindRelation(person,target):
  #people 아래 트리 쪽에 target이 있다고 가정
  visited = [False for _ in range(len(relationInfo))];

  queue = deque();
  queue.append(person);
  found = False;
  relation = 0;
  while queue:
    for _ in range(len(queue)):
      
      elem = queue.popleft();
      # print("elem : {}".format(elem));
      if visited[elem]: continue;
      visited[elem] = True;

      if elem == target:
        found = True; break;
      
      #queue에 아이템 넣기
      for item in relationInfo[elem]:
        if visited[item]: continue;
        queue.append(item);
      
      if parentInfo[elem] != -1:
        if visited[parentInfo[elem]]: continue;
        queue.append(parentInfo[elem]);

    if found: break;

    #촌수 증가
    relation += 1;
      
  if found: return relation;
  else: return -1;



  
  
  
  


#=== main function ===#
people = int(input());

relationInfo = [[] for _ in range(people+1)];
parentInfo = [-1 for _ in range(people+1)];

target = list(map(int,input().split()));

for _ in range(int(input())):
  parent, child = map(int,input().split());
  parentInfo[child] = parent;
  relationInfo[parent].append(child);

print(FindRelation(target[0],target[1]));






