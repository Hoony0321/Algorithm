def solution(money):
    #첫번째 집 포함
    dp1 = [[0,0] for _ in range(len(money))]
    dp1[0][0] = -10000
    dp1[0][1] = money[0]
    
    #첫번째 집 미포함
    dp2 = [[0,0] for _ in range(len(money))]
    dp2[0][0] = 0
    dp2[0][1] = -10000
    
    for i in range(1, len(money)):
        dp1[i][0] = max(dp1[i-1])
        dp1[i][1] = money[i] + dp1[i-1][0]
        dp2[i][0] = max(dp2[i-1])
        dp2[i][1] = money[i] + dp2[i-1][0]    
    
    return max(dp1[len(money)-1][0], dp2[len(money)-1][0], dp2[len(money)-1][1])