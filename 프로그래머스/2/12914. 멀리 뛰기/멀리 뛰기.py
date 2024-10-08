def solution(n):
    
    dp = [1 for _ in range(n+1)]
    
    if n < 3:
        return 2 if n==2 else 1
    
    dp[1] = 1
    dp[2] = 2
    
    for i in range(3,n+1):
        dp[i] = dp[i-1] + dp[i-2]
        
    return dp[n] % 1234567