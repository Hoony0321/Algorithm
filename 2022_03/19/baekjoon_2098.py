#baekjoon_2098_외판원 순회

N = int(input());

W = [[0] * N for _ in range(N)];
dp = [[None for _ in range(1 << N)] for _ in range(N)];

for i in range(N):
    W[i] = list(map(int,input().split()));

def TSP(current, visited):

    if visited == (1 << N) - 1: #모든 도시 방문 완료
        return float('INF') if W[current][0] == 0 else W[current][0];

    if dp[current][visited] != None:
        return dp[current][visited];
    min_weight = float('INF');
    for nextV in range(N):
        if W[current][nextV] == 0: continue; #존재하지 않은 간선
        if visited & (1 << nextV) != 0: continue; #이미 방문한 도시
        min_weight = min(min_weight, W[current][nextV] + TSP(nextV, visited | (1 << nextV)));

    dp[current][visited] = min_weight;
    return dp[current][visited];

print(TSP(0,1));





