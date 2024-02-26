from collections import Counter
from itertools import combinations

def solution(weights):
    answer = 0
    counter = Counter(weights)
    
    # 같은 무게
    for key, value in counter.items():
        if(value == 1): continue
        answer += value * (value-1) // 2
    
    # 다른 무게
    weightSet = set(weights)
    for weight in weightSet:
        if weight * 2/3 in counter:
            answer += counter[weight*2/3] * counter[weight]
        if weight * 2/4 in counter:
            answer += counter[weight*2/4] * counter[weight]
        if weight * 3/4 in counter:
            answer += counter[weight*3/4] * counter[weight]
    
    return answer