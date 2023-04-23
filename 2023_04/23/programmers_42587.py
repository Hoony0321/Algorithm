#문제정보
#programmers_42587 - 프로세스 (난이도 2)

from collections import deque
def solution(priorities, location):
    queue = deque()
    
    for i in range(len(priorities)):
        queue.append((priorities[i],i))
    
    maxPriority = max(queue, key= lambda x : x[0])[0]
    
    count = 0
    while(1):
        priority, order = queue.popleft()
            
        if(maxPriority == priority):
            count += 1
            if(order == location): break
            maxPriority = max(queue, key= lambda x : x[0])[0]
            
        
        else:
            queue.append([priority, order])
        
    
    return count