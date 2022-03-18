#baekjoon_2293_동전1

N , K = map(int,input().split()); # N 동전 가짓수 , K 목표 금액

coins = [];
for _ in range(N):
    coins.append(int(input()));

dp = [0 for _ in range(K+1)]; #dp[i] = i까지 나올 수 있는 합.
dp[0] = 1;

for coin in coins:
    for i in range(coin,K+1):
        dp[i] += dp[i - coin];

print(dp[K]);







