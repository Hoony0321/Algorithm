import math
def solution(a):
    MOD = 10**7 + 19
    r,c = len(a), len(a[0])
    one_counts = [sum(row[i] for row in a) for i in range(c)]
    
    # precompute nCr values
    comb = [[0 for _ in range(r+1)] for _ in range(r+1)]
    for i in range(r+1):
        for j in range(0,i+1):
            comb[i][j] = math.comb(i,j) % MOD
            
    # init dp
    dp = [[0 for _ in range(r+1)] for _ in range(c+1)]
    dp[1][one_counts[0]] = comb[r][one_counts[0]]
    
    # main process
    for i in range(1,c):
        for j in range(0,r+1):
            if dp[i][j] == 0 : continue
            one_count = one_counts[i]
            for k in range(0,one_count+1):
                if k > j or one_count-k > r-j: continue
                case_comb = (comb[j][k] * comb[r-j][one_count-k]) % MOD
                next_j = j - k + one_count - k
                dp[i+1][next_j] = (dp[i+1][next_j] + case_comb * dp[i][j]) % MOD
    
    
    return dp[c][0]