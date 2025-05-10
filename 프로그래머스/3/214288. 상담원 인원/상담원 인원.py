import heapq
from collections import deque
def solution(k, n, reqs):
    
    def generateGroups():
        result = []
        def backtracking(current,remaining,depth):
            if depth == k:
                if remaining == 0:
                    result.append([x+1 for x in current])
                return
            
            for i in range(remaining+1):
                backtracking(current + [i],remaining - i, depth + 1)
        
        backtracking([],n-k,0)
        return result
    
    def getTotalDuration(group):
        totalDuration = 0
        timeQueue = []
        for req in reqs:
            heapq.heappush(timeQueue,req) # [startTime,duration,mentoType] or [finishTime,mentoType]
        
        waitingList = [deque([]) for _ in range(k+1)] # [startTime, duration]
        activeMentos = group
        
        while timeQueue:
            heapElem = heapq.heappop(timeQueue)
            
            if len(heapElem) == 2: # case : finish consulting
                time, mentoType = heapElem
                activeMentos[mentoType] += 1
                if waitingList[mentoType]:
                    startTime,duration = waitingList[mentoType].popleft()
                    heapq.heappush(timeQueue,[time + duration,mentoType])
                    activeMentos[mentoType] -= 1
                    totalDuration += time - startTime
            elif len(heapElem) == 3: # case : new consulting
                time, duration, mentoType = heapElem
                if activeMentos[mentoType] > 0:
                    activeMentos[mentoType] -= 1
                    heapq.heappush(timeQueue,[time + duration,mentoType])
                else:
                    waitingList[mentoType].append([time,duration])
        
        return totalDuration
        
    groups = generateGroups()
    minTotalDuration = float('inf')
    for group in groups:
        duration = getTotalDuration([0] + group)
        minTotalDuration = min(duration,minTotalDuration)
    
    return minTotalDuration