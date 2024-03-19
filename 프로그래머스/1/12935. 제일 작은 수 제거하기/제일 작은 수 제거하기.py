def solution(arr):
    answer = []
    
    minNum = float('INF')
    for num in arr:
        minNum =  min(minNum, num)
    
    for i in range(len(arr)):
        if arr[i] == minNum: continue
        answer.append(arr[i])
    
    if len(answer) == 0:
        answer.append(-1)
    
    return answer