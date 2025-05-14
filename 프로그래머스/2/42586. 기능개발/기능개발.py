from collections import deque
import math
def solution(progresses, speeds):
    answer = []
    queue = deque()
    for i in range(len(progresses)):
        requireDay = math.ceil((100 - progresses[i]) / speeds[i])
        queue.append(requireDay)
        
    while queue:
        num = 0
        targetDay = queue[0]
        
        while queue and queue[0] <= targetDay:
            queue.popleft()
            num += 1
        
        answer.append(num)
        
    
    return answer