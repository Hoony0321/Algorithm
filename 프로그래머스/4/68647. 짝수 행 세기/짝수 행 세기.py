import math

def solution(a):
    MOD = 10**7 + 19
    r, c = len(a), len(a[0])
    
    # 1. 각 열의 1의 개수 세기
    one_counts = [sum(row[i] for row in a) for i in range(c)]
    
    # 2. nCr 테이블 미리 만들기 (효율성 및 모듈러 적용)
    comb = [[0] * (r + 1) for _ in range(r + 1)]
    for i in range(r + 1):
        comb[i][0] = 1
        for j in range(1, i + 1):
            comb[i][j] = (comb[i-1][j-1] + comb[i-1][j]) % MOD

    # 3. DP 배열 (dp[열][짝수 개수가 j개인 행의 수])
    dp = [[0 for _ in range(r + 1)] for _ in range(c + 1)]
    
    # 초기값: 0번째 열 처리
    dp[1][r - one_counts[0]] = comb[r][one_counts[0]]
    
    for i in range(1, c): # i는 현재 열 인덱스 (0부터 시작 기준 i+1번째 열 작업)
        count = one_counts[i]
        for j in range(r + 1): # j: 이전까지 짝수였던 행의 개수
            if dp[i][j] == 0: continue
            
            # k: 짝수였던 j개의 행 중에서 1을 배정할 행의 개수
            for k in range(count + 1):
                if k > j or (count - k) > (r - j): continue
                
                # 새로운 짝수 행의 개수 계산
                # 짝수(j)였는데 1이 들어오면(k) -> 홀수가 됨
                # 홀수(r-j)였는데 1이 들어오면(count-k) -> 짝수가 됨
                next_j = (j - k) + (count - k)
                
                case_count = (comb[j][k] * comb[r-j][count-k]) % MOD
                dp[i+1][next_j] = (dp[i+1][next_j] + dp[i][j] * case_count) % MOD
                
    return dp[c][r] # 모든 행이 짝수인 경우 (문제에 따라 0일수도, r일수도 있음)