#baekjoon_5557_1학년
N = int(input());
S = list(map(int,input().split()));

dp = [[0 for _ in range(21)] for _ in range(N)]

dp[0][S[0]] = 1;

for i in range(N-2): #N-2까지만 하면 됨.
    for j in range(21):

        if dp[i][j] == 0: continue;

        #더하기
        sum = j + S[i+1]
        if sum <= 20:
            dp[i+1][sum] += dp[i][j]
        #빼기
        sum = j - S[i+1]
        if sum >= 0:
            dp[i+1][sum] += dp[i][j]

print(dp[N-2][S[-1]]);



