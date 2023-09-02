def solution(land):
    answer = 0
    dp = [[0 for _ in range(4)] for _ in range(len(land))]
    
    for i in range(4):
        dp[0][i] = land[0][i]

    def get_max_score(y,x):
        max_prev_score = 0
        for k in range(4):
            if(k == x): continue
            if(max_prev_score < dp[y-1][k]):
                max_prev_score = dp[y-1][k]
        dp[y][x] = max_prev_score + land[y][x]
    
    for i in range(1,len(land)):
        for j in range(4):
            get_max_score(i,j)
    
    
    return max(dp[len(land)-1])