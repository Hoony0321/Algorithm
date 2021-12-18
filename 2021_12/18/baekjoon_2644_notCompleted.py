#baekjoon_2644_촌수계산

#=== import module ===#

#=== variable declare ===#
parents = [];
#=== Function define ===#
def FindRelation(people1,people2):
  
  relation = 0;
  find = False;
  while(1):
    relation += 1;
    parent = parents[people1];
    if parent == None: break;
    elif parent == people2: find = True; break;
    else: 
      people1 = parent;
  
  if not find: return -1;
  else: return relation;
  
  


#=== main function ===#
people = int(input());

parents = [[] for _ in range(people+1)];

target = list(map(int,input().split()));

for _ in range(int(input())):
  parent, child = map(int,input().split());
  parents[child] = parent;

result = FindRelation(target[0],target[1]);
if result != -1: print(result); exit(0);

result = FindRelation(target[1],target[0]);
if result != -1: print(result); exit(0);

print(result);






