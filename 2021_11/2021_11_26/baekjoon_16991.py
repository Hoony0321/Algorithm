#baekjoon_16991_외판원 순회 3

#=== import module ===#
import math
#=== Function define ===#
def ReturnDist(idx1,idx2):
  global distInfo;
  p1 = distInfo[idx1]; p2 = distInfo[idx2];

  sum = (p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2;
  return math.sqrt(sum);

def TPS(current,visited):
  global N,dp,w,VISITED_ALL,INF;

  if visited == VISITED_ALL: #모든 지점 방문함.
    return w[current][0];
  
  if dp[current][visited] != None: #이미 계산된 값이 있음
    return dp[current][visited];
  
  #새로운 경로
  weight = INF;
  for city in range(N):
    if w[current][city] == 0 : continue; #갈 수 없는 경로
    if visited & (1 << city) != 0: continue; #이미 방문한 도시
    
    weight = min(weight, TPS(city, visited | (1 << city)) + w[current][city] );
  dp[current][visited] = weight;
  return weight;



#=== variable declare ===#
N = 0; dp = []; w = []; distInfo = [];
#=== main function ===#
N = int(input());

for _ in range(N):
  distInfo.append(list(map(int,input().split())));

w = [[0 for i in range(N)] for j in range(N)];
dp = [[None for i in range(1 << N) ] for j in range(N)];

VISITED_ALL = (1 << N) - 1;
INF = float('inf');

#거리 비용 계산
for i in range(N-1):
  for j in range(i+1,N):
    dist = ReturnDist(i,j);
    w[i][j] = dist; w[j][i] = dist;

print(TPS(0,1));

