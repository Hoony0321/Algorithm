#baekjoon_9095_1,2,3더하기

T = int(input());
dp = [0 for _ in range(11)];
dp[1] = 1;
dp[2] = 2;
dp[3] = 4;

def RecursionFunc(N):

    if dp[N] == 0:
        dp[N] = RecursionFunc(N-1) + RecursionFunc(N-2) + RecursionFunc(N-3);

    return dp[N];

for _ in range(T):
    target = int(input());

    print(RecursionFunc(target));