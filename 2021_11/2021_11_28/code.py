#baekjoon

#=== import module ===#

#=== variable declare ===#
N = 0; arr1 = []; arr2 = []; visited = [];
#=== Function define ===#
def DFS(current, selected, sum):
    if current in must_select: return;
    if current in visited: return;

    sum = [0 for _ in range(N+1)];
    




#=== main function ===#
N = int(input());

arr1 = [i for i in range(1,N+1)];
for _ in range(N):
  arr2.append(int(input()));

must_select  = []; #무조건 뽑아야 하는 거
for i in range(N):
  if arr[i] == i:
    must_select.append(i);

for i in range(N):
  DFS(i,[]);
    