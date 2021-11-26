#baekjoon_2098_외판원 순회

#=== import module ===#

#=== Function define ===#
def TSP(current, visited):
  global N,w,dp, VISITED_ALL,INF;

  
  if visited == VISITED_ALL: #모든 곳 방문 완료
    result = w[current][0] if w[current][0] != 0 else INF;
    
    return result;
  
  if dp[current][visited] != None: #이미 방문했던 경로임.
    return dp[current][visited];
  
  #새로 방문하는 경로
  weight = INF;
  for city in range(N):
    if current == city : continue; #자기 자신 도시로 가지 않음.
    if w[current][city] == 0 : continue; #현재 경로에서 해당 도시로 가능 경로 없음
    if visited & (1 << city) != 0 : continue; #이미 방문했던 도시임.

    weight = min(weight, TSP(city,visited | (1 << city)) + w[current][city]);
  dp[current][visited] = weight;
  return weight;  


  



#=== variable declare ===#
N = 0; w = []; dp = []; 

#=== main function ===#
N = int(input());
for _ in range(N):
  w.append(list(map(int,input().split())));

dp = [ [None] * (1 << N) for _ in range(N)];
VISITED_ALL = (1 << N) -1;
INF = float('INF');

#current, visited, cost
print(TSP(0,1));