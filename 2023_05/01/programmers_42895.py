#문제설명
#programmers_42895 - N으로 표현 (난이도 2)

from collections import deque

def solution(N, number):
    
    if(N == number):
        return 1
    dp = [set() for _ in range(8)]
    
    for i in range(8):
        dp[i].add(int(str(N) * (i+1)))
        
    for i in range(1,8): #N을 i+1 사용한 경우의 수 구하기
        tmpSet = dp[i].copy()
        for j in range(i+1): #N을 j+1 사용한 경우 + N을 i-j 사용한 경우 더하기
            op1s = dp[j]
            op2s = dp[i-j-1]
            for op1 in op1s:
                for op2 in op2s:
                    tmpSet.add(op1 + op2)
                    tmpSet.add(op1 - op2)
                    tmpSet.add(op1 * op2)
                    if(op2 != 0):
                        tmpSet.add(op1 // op2)
            
        if(number in tmpSet):
            return i+1
        else:
            dp[i] = tmpSet
        
    
    return -1