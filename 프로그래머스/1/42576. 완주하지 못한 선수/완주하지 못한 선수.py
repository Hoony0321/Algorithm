from collections import defaultdict
def solution(participant, completion):
    answer = ''
    
    compDict = defaultdict(int)
    for c in completion:
        compDict[c] += 1
    
    for p in participant:
        compDict[p] -= 1
        if compDict[p] < 0:
            answer = p
            break
    
    
    return answer