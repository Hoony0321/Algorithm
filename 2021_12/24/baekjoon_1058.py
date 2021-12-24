#baekjoon_1058_친구

#=== import module ===#
from collections import deque
#=== variable declare ===#

#=== Function define ===#
def BFS(num,people):
  queue = deque(friendInfo[num]);
  dp[num] = deque(friendInfo[num]);
  
  while queue:
    peek = queue.popleft();
    for elem in friendInfo[peek]:
      dp[num].append(elem);

  dp[num] = set(dp[num]);



  return len(dp[num]);

  

def solve(people):
  maxVal = 0;

  for num in range(1,people+1):
    result = BFS(num,people);
    if result > maxVal: maxVal = result;
  
  if maxVal == 0: print(maxVal);
  else: print(maxVal-1);

#=== main function ===#
people = int(input());

friendInfo = [[] for _ in range(people+1)];
dp = [ [] for _ in range(people+1)];

for i in range(1,people+1):
  inputData = input();
  for j in range(len(inputData)):
    if inputData[j] == 'Y':
      friendInfo[i].append(j+1);

solve(people);
      