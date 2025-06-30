from collections import deque
import math
def solution(players, m, k):
    answer = 0
    ns = 0 # 서버 개수
    dst = deque() # 사라질 서버 타이머
    
    for t in range(24):
        # 서버 개수 확인
        if dst and dst[0][0] <= t:
            ns -= dst[0][1]
            dst.popleft()
        
        # 필요한 서버 개수
        rs = players[t] // m - ns
        
        # 서버 증설
        if rs > 0:
            dst.append([t+k,rs])
            ns += rs
            answer += rs
        
    
    return answer