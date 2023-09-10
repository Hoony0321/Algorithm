import heapq

def solution(n, works):
    if sum(works) <= n:
        return 0
    
    max_heap = []
    for time in works:
        heapq.heappush(max_heap, -time)
    
    while(n > 0):
        max_value = heapq.heappop(max_heap)
        heapq.heappush(max_heap,max_value + 1)
        n -= 1
    
    sum_time = 0
    for time in max_heap:
        sum_time += time ** 2
    
    return sum_time