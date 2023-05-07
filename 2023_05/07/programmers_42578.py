#문제설명
#programmers_42578 - 의상 (난이도 2)

def solution(clothes):
    answer = 1
    clothDict={}
    
    for cloth in clothes:
        if cloth[1] in clothDict:
            clothDict[cloth[1]].append(cloth[0])
        else:
            clothDict[cloth[1]] = [cloth[0]]
            
    for key, value in clothDict.items():
        answer *= (len(value)+1)
    
    return answer-1