#baekjoon_11058_크리보드

N = int(input()); #버튼 누르는 횟수

if N <= 6:
    print(N);
    exit(0);

dp = [0 for _ in range(N+1)];
dp[1] = 1;
dp[2] = 2;
dp[3] = 3;
dp[4] = 4;
dp[5] = 5;
dp[6] = 6;

for i in range(7,N+1): #7부터 N까지 진행
    j = 3;
    while(i-j > 1):
        dp[i] = max(dp[i], dp[i-j] * (j-1));
        j += 1;

print(dp[N]);