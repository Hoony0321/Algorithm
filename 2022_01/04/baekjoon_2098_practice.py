#baekjoon_2098_외판원 

#=== import module ===#

#=== variable declare ===#
N = -1; #도시의 수
W = []; #비용 행렬
dp = []; #dp 행렬
#=== Function define ===#
def TSP(current, visited):
  global N;

  if visited == ((1 << N) -1): #모든 지점 방문 완료
    return float('INF') if W[current][0] == 0 else W[current][0];

  if dp[current][visited] != None:
    return dp[current][visited];
  
  min_weight = float('INF');
  for i in range(N):
    if visited & (1 << i) != 0: continue; #이미 방문한 도시
    if W[current][i] == 0 : continue; #방문하는 루트가 없는 도시.
    min_weight = min(min_weight, W[current][i] + TSP(i, visited | (1 << i)));
  
  dp[current][visited] = min_weight;
  return min_weight;


#=== main function ===#
N = int(input());

dp = [[None for _ in range(1 << N)] for _ in range(N)];

for _ in range(N):
  W.append(list(map(int,input().split())));

print(TSP(0,1)); #0에서 출발



