from collections import deque
def solution(strs, t):
    # init variables
    MAX_WORD_SIZE = 5
    MAX_VALUE = 100 * 5 * 20000
    strs_set = set(strs)
    dp = [MAX_VALUE for _ in range(len(t)+1)]
    dp[0] = 0
    
    # i는 완성된 글자 개수, j는 글자 개수
    # main process
    for i in range(1,len(t)+1):
        for j in range(1,min(i+1,MAX_WORD_SIZE+1)):
            if t[i-j:i] in strs_set and dp[i-j] != MAX_VALUE:
                dp[i] = min(dp[i], dp[i-j] + 1)
    
    return dp[len(t)] if dp[len(t)] != MAX_VALUE else -1