#이항계수 구하기 (동적 계획법 사용)

n, k = map(int,input().split());

dp = [[1 for _ in range(n+1)] for _ in range(k+1)]


for i in range(n+1): #0부터 n까지
    for j in range(min(i,k)+1): #0부터 min(i,k)까지
        if j == 0 or j == 1 or i == 0 or i == 1: continue;
        print(i,j);
        dp[i][j] = dp[i-1][j-1] + dp[i-1][j-1];

print(dp[n][k]);