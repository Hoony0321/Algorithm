from collections import deque
def solution(s):
    n = len(s)
    if n <= 1 or s == s[::-1]:  # 전체가 팰린드롬이면 바로 반환
        return n

    max_len = 1

    # 중앙에서 확장 (홀수 길이와 짝수 길이)
    for c in range(n - 1):
        # 홀수 길이: 중심 하나(c)
        l = r = c
        while l >= 0 and r < n and s[l] == s[r]:
            cur = r - l + 1
            if cur > max_len:
                max_len = cur
            l -= 1
            r += 1

        # 짝수 길이: 중심 사이(c, c+1)
        l, r = c, c + 1
        while l >= 0 and r < n and s[l] == s[r]:
            cur = r - l + 1
            if cur > max_len:
                max_len = cur
            l -= 1
            r += 1

    return max_len
