#문제설명
#programmers_12953 - N개의 최소공배수 (난이도 2)

def solution(arr):
    MAX = max(arr)

    while True:
        cnt = 0
        MAX += 1

        for a in arr:
            if MAX%a == 0:
                cnt += 1
        if cnt == len(arr):
            break
    return MAX