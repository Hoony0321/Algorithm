from collections import deque

def solution(prices):
    answer = [-1 for _ in range(len(prices))]
    stack = deque()
    
    for time,price in enumerate(prices):
        while stack and stack[0][1] > price:
            idx,_ = stack.popleft()
            answer[idx] = time - idx
        stack.appendleft([time, price])
    
    for idx,time in enumerate(answer):
        if answer[idx] == -1:
            answer[idx] = len(prices) - idx - 1

    return answer