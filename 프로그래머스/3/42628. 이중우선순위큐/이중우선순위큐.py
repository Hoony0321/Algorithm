import heapq

def solution(operations):
    maxQueue = []
    minQueue = []
    
    for operation in operations:
        operator, number = operation.split(" ")
        
        if(operator == 'I'):
            heapq.heappush(maxQueue, -int(number))
            heapq.heappush(minQueue, int(number))
        elif(operator == 'D' and minQueue):
            if(number == '1'): #최댓값 삭제
                heapq.heappop(maxQueue)
                minQueue = [-x for x in maxQueue]
                heapq.heapify(minQueue)
            elif(number == '-1'): #최솟값 삭제
                heapq.heappop(minQueue)
                maxQueue = [-x for x in minQueue]
                heapq.heapify(maxQueue)
    
    if not maxQueue:
        return [0,0]
    answer = [-maxQueue[0], minQueue[0]]
    return answer