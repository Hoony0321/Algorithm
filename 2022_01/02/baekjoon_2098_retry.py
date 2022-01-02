#baekjoon_2098_외판원 (다시 한번 해보기)
#역산하듯이 올라가면서 dp값 채우는 방식 꼭 기억해야할 것!
#=== import module ===#

#=== variable declare ===#
W = [];#비용 행렬 
N = -1;#도시의 개수
dp = [];#가지치기
#=== Function define ===#
def TSP(curNode, visited):
  global N;

  if visited == (1 << N) - 1: #모든 지점 방문 완료/ 원래 지점으로 복귀
    if W[curNode][0] != 0: return W[curNode][0];
    else: return float('INF');
     

  minWeight = float('INF');

  if dp[curNode][visited] != None: return dp[curNode][visited];

  for nextNode in range(N):
    if visited & (1 << nextNode) != 0: continue; #이미 방문한 지점
    if W[curNode][nextNode] == 0 : continue; #현 지점에서 못 가는 지점
    minWeight = min(minWeight, W[curNode][nextNode] + TSP(nextNode, visited | (1 << nextNode)));
  
  dp[curNode][visited] = minWeight;
    

  return minWeight;


#=== main function ===#
N = int(input());
dp = [[None for _ in range(1 << N)] for _ in range(N)];
for _ in range(N):
  W.append(list(map(int,input().split())));

print(TSP(0,1));