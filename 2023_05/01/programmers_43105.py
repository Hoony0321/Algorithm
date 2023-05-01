#문제설명
#programmers_43105 - 정수 삼각형 (난이도 3)

import copy
def solution(triangle):
    dp = copy.deepcopy(triangle)
    
    for i in range(1, len(dp)):
        for j in range(len(dp[i])):
            if(j-1 < 0): #왼쪽 끝
                dp[i][j] = dp[i-1][j] + dp[i][j]
            elif(j == len(dp[i])-1): #오른쪽 끝
                dp[i][j] = dp[i-1][j-1] + dp[i][j]
            else: #중간
                dp[i][j] = max(dp[i-1][j-1] + dp[i][j], dp[i-1][j] + dp[i][j])
    
    return max(dp[-1])