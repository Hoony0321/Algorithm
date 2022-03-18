#baekjoon_12026_BOJ거리

N = int(input());
road = [0] + list(input()); #index 1부터 데이터 넣기 위함.
DP = [float('INF') for _ in range(N+1)]; DP[1] = 0;
order = {'B' : 'O' , 'O' : 'J', 'J' : 'B'};
for i in range(1,N): #1부터 N-1까지 탐색 시작
    if i != 1 and DP[i] == float('INF'): continue; #이동 불가능한 지점.

    roadVal = order[road[i]];

    for j in range(i+1,N+1): #i+1부터 N까지 탐색

        if road[j] != roadVal: #다른 블럭 - 이동 불가
            continue;

        DP[j] = min(DP[j] , DP[i] + (j-i) ** 2);

if DP[N] == float('INF'): print(-1);
else: print(DP[N]);