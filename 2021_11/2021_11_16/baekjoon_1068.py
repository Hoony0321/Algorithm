#baekjoon_1068_트리

#=== import module ===#
  

#=== Function define ===#

#=== variable declare ===#
num_node = 0;
node_parentInfo = [];
node = [];
#=== main function ===#
num_node = int(input());
nodes = [[] for _ in range(num_node)];

#각 노드 부모 정보 받기
node_parentInfo = list(map(int,input().split()));

#부모 정보 입력
for i in range(num_node):
  if(node_parentInfo[i] != -1):
    nodes[node_parentInfo[i]].append(i);


remove_node_idx = int(input());
remove_node = [remove_node_idx];

idx = 0;
while(idx < len(remove_node)):
  remove_node +=  nodes[remove_node[idx]];
  idx += 1;

for idx in remove_node:
  if node_parentInfo[idx] == -1: continue;
  nodes[node_parentInfo[idx]].remove(idx);

count = 0;
for i in range(num_node):
  if not i in remove_node and len(nodes[i]) == 0:
    count += 1;

print(count);
  







