def solution(temperature, t1, t2, a, b, onboard):
    OFFSET = 10
    MAX = float('inf')

    # 온도 보정 (0 <= 온도 <= 50)
    t1 += OFFSET
    t2 += OFFSET
    temperature += OFFSET

    n = len(onboard)
    dp = [[MAX] * 51 for _ in range(n)]
    dp[0][temperature] = 0

    for i in range(n - 1):
        for temp in range(51):
            if dp[i][temp] == MAX:
                continue

            # 탑승 중인데 쾌적 온도 범위를 벗어난 경우 skip
            if onboard[i] and not (t1 <= temp <= t2):
                continue

            # 에어컨 ON
            if temp + 1 <= 50: # 희망온도 > 실내온도
                dp[i + 1][temp + 1] = min(dp[i + 1][temp + 1], dp[i][temp] + a)
            if temp - 1 >= 0: # 희망온도 < 실내온도
                dp[i + 1][temp - 1] = min(dp[i + 1][temp - 1], dp[i][temp] + a)
            # 희망온도 = 실내온도
            dp[i + 1][temp] = min(dp[i + 1][temp], dp[i][temp] + b)

            # 에어컨 OFF
            if temperature > temp and temp + 1 <= 50: # 실외온도 > 실내온도
                dp[i + 1][temp + 1] = min(dp[i + 1][temp + 1], dp[i][temp])
            elif temperature < temp and temp - 1 >= 0: # 실외온도 < 실내온도
                dp[i + 1][temp - 1] = min(dp[i + 1][temp - 1], dp[i][temp])
            else: # 실외온도 = 실내온도
                dp[i + 1][temp] = min(dp[i + 1][temp], dp[i][temp])

    # 마지막 시점에서 온도가 쾌적 범위 내에 있는 최소값 반환
    if onboard[n-1]:
        answer = min(dp[n-1][t] for t in range(t1,t2+1))
    else:
        answer = min(dp[n-1])
    return answer