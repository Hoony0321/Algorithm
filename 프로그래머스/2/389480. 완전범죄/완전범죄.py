from collections import deque

def solution(info, n, m):
    dp = [[float('inf') for _ in range(3 * len(info)+1)] for _ in range(len(info))]
    
    queue = deque()
    queue.append([0,0,-1]) # sumA, sumB, depth
    
    while queue:
        sumA, sumB, depth = queue.popleft()
        if depth+1 >= len(info): # last depth
            continue
        
        # A가 훔치는 경우
        nSumA = sumA + info[depth+1][0]
        nSumB = sumB

        if nSumA < n and dp[depth+1][nSumB] > nSumA:
            queue.append([nSumA, nSumB, depth+1])
            dp[depth+1][nSumB] = nSumA

        # B가 훔치는 경우
        nSumA = sumA 
        nSumB = sumB + info[depth+1][1]

        if nSumB < m and dp[depth+1][nSumB] > nSumA:
            queue.append([nSumA, nSumB, depth+1])
            dp[depth+1][nSumB] = nSumA
        
    answer = min(dp[len(info)-1])
    if answer == float('inf'):
        answer = -1
    return answer