from collections import deque
import heapq
def solution(priorities, location):
    answer = 0
    queue = deque()
    maxPQ = []
    
    for i,p in enumerate(priorities):
        queue.append([i,p]) # index, priority
        heapq.heappush(maxPQ,-p)

    while maxPQ:
        targetP = -heapq.heappop(maxPQ)

        
        while queue[0][1] != targetP:
            elem = queue.popleft()
            queue.append(elem)

        answer += 1
        i,p = queue.popleft()
        if i == location:
            break
        

    return answer