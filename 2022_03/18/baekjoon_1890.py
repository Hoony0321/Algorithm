#baekjoon_1890_점프
from collections import deque





N = int(input());

MapInfo =[[] * N for _ in range(N)];
dp = [[0] * N for _ in range(N)];
dp[0][0] = 1;
for i in range(N):
    MapInfo[i] = list(map(int,input().split()));

for i in range(N):
    for j in range(N):
        if dp[i][j] == 0: continue;
        if MapInfo[i][j] == 0: continue;
        delta = MapInfo[i][j];

        #오른쪽 이동
        ny = i; nx = j + delta;
        if nx < N:
            dp[ny][nx] += dp[i][j];
        #왼쪽 이동
        ny = i + delta; nx = j;
        if ny < N:
            dp[ny][nx] += dp[i][j];

print(dp[N-1][N-1]);


