from collections import defaultdict
def solution(participants, completions):
    answer = ''
    completionDict = defaultdict(int)
    for key in completions:
        completionDict[key] += 1
    
    for participant in participants:
        completionDict[participant] -= 1
        if completionDict[participant] < 0:
            return participant