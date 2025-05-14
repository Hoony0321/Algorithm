
def solution(arr):
    answer = []
    lastNum = -1
    for num in arr:
        if lastNum == num:
            continue
        answer.append(num)
        lastNum = num

    return answer