import math
def solution(arr):
    answer = -1
    num_arr = [int(arr[2*i]) for i in range(math.ceil(len(arr) / 2))]
    op_arr = ['+'] + [arr[2*i+1] for i in range(math.floor(len(arr) / 2))]
    n = len(num_arr)
    
    max_dp = [[float('-inf') for _ in range(n)] for _ in range(n)]
    min_dp = [[float('inf') for _ in range(n)] for _ in range(n)]
    
    for i in range(n):
        max_dp[i][i] = num_arr[i]
        min_dp[i][i] = num_arr[i]
    
    for k in range(1,n):
        for i in range(0,n-k):
            for j in range(i,i+k):
                if op_arr[j+1] == '+':
                    max_dp[i][i+k] = max(max_dp[i][i+k], max_dp[i][j] + max_dp[j+1][i+k])
                    min_dp[i][i+k] = min(min_dp[i][i+k], min_dp[i][j] + min_dp[j+1][i+k])
                if op_arr[j+1] == '-':
                    max_dp[i][i+k] = max(max_dp[i][i+k], max_dp[i][j] - min_dp[j+1][i+k])
                    min_dp[i][i+k] = min(min_dp[i][i+k], min_dp[i][j] - max_dp[j+1][i+k])
    

    
    
    return max_dp[0][n-1]