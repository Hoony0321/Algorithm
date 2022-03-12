#baekjoon_1029_그림교환

#=== import module ===#
from collections import deque
#=== variable declare ===#
dp = [];
#=== Function define ===#
def BFS():
  queue = deque();
  queue.append([0,1]); #curPrice, curPerson

  while queue:
    for _ in range(len(queue)):
      curPrice, curPerson = queue.popleft();

      





  
    


#=== main function ===#
N = int(input()) #아티스트 수
info = [list(map(int,list(input()))) for _ in range(N)];
max_person = 1;
dp = [[None for _ in range(1 << N)] for _ in range(10)]
dp[0][1] = 1;
BFS();
print(max_person);


