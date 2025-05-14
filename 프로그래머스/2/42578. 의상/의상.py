from collections import defaultdict
def solution(clothes):
    answer = 1
    clothesDict = defaultdict(int)
    
    for name,clothesType in clothes:
        clothesDict[clothesType] += 1
    
    for key,value in clothesDict.items():
        answer *= (value + 1)
        
        
    
    
    return answer-1