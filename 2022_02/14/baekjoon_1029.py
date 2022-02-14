#baekjoon_1029_그림교환

#=== import module ===#
from collections import deque
#=== variable declare ===#
dp = [];
#=== Function define ===#
def DFS(curPrice, curPerson, curVisited):
  global N

  if dp[curPerson][curPrice][curVisited] == None: #예전에 계산해놓은 값 존재 X
    max_result = 0;
    for nextPerson in range(N):
      if curVisited & (1 << nextPerson) != 0: continue; #이미 방문한 적 있음.
      if curPrice > info[curPerson][nextPerson] : continue; #조건 만족 X
      max_result = max(max_result, DFS(info[curPerson][nextPerson],
        nextPerson, curVisited | (1 << nextPerson)) +1 );
    dp[curPerson][curPrice][curVisited] = max_result;      
  
  if dp[curPerson][curPrice][curVisited] == None: #더 이상 진행X
    dp[curPerson][curPrice][curVisited] = 0;


  return dp[curPerson][curPrice][curVisited];


  
  
  

      



#=== main function ===#
N = int(input()) #아티스트 수
info = [list(map(int,list(input()))) for _ in range(N)];
dp = [[[None for _ in range(1 << N)] for _ in range(10)] for _ in range(N)];

print(DFS(0,0,1) + 1);




