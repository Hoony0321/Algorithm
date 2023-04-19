#문제정보
#programmers_12914 - 멀리뛰기 (난이도 2)

def solution(n):
    if(n <= 2):
        return n
    
    answer = 0
    
    dp = [-1 for _ in range(n+1)]
    dp[0] = 0
    dp[1] = 1
    dp[2] = 2
    
    
    count = 3
    while(count <= n):
        dp[count] = dp[count-1] + dp[count-2]
        count += 1
    
    answer = dp[n] % 1234567
    
    
    return answer