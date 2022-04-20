#Floyd 최단 경로 찾기

def Floyd(fromV, toV):
    global n; #정정 개수
    for k in range(1,n+1): #1부터 n까지
        for i in range(1,n+1):
            for j in range(1, n+1):
                dp[k][i][j] = min( dp[k-1][i][j], dp[k-1][i][k] + dp[k-1][k][j] );


    return dp[n][fromV][toV];




n = 5;
W = [[float('INF') for _ in range(n+1)] for _ in range(n+1)];
P = [[0 for _ in range(n+1)] for _ in range(n+1)];

W[1][2] = 1; W[1][4]=1; W[1][5]=5; W[2][1] = 9; W[2][3] = 3; W[2][4] = 2; W[3][4] = 4; W[4][3] = 2; W[4][5] = 3; W[5][1]=3;




dp = [[[float('INF') for _ in range(n+1)] for _ in range(n+1)] for _ in range(n+1)];
dp[0][1][2] = 1; dp[0][1][4]=1; dp[0][1][5]=5; dp[0][2][1] = 9; dp[0][2][3] = 3; dp[0][2][4] = 2; dp[0][3][4] = 4; dp[0][4][3] = 2; dp[0][4][5] = 3; dp[0][5][1]=3;
for i in range(1,n+1):
    dp[0][i][i] = 0;


print(Floyd(2,5));
for row in dp[n]:
    for elem in row:
        print(elem, end=' ');
    print();