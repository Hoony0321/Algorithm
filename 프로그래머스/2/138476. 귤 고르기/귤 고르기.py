from collections import Counter
from queue import PriorityQueue
def solution(k, tangerine):
    answer = 0
    
    countDict = Counter(tangerine)
    queue = PriorityQueue()
    
    for key, value in countDict.items():
        queue.put([-value, key])
        
    while not queue.empty() and k > 0:
        value, key = queue.get()
        k += value
        answer += 1
    
    return answer